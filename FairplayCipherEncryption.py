# Encrypts a message using a cipher based on the FairPlay table.

# Third Party Imports
from num2words import num2words
import numpy as np
import sys
import time
import math

# Local Imports
import FairPlayTable

def GetDataFromFile(textfile):
    try:
        # Open the file in read mode
        # Name of the file should be "plaintext.txt"
        with open(textfile, "r") as file:
            lines = file.readlines()

        key = lines[0].strip()
        plaintext = " ".join(lines[1:]).strip()

        return (key, plaintext)
    except:
        print("ERROR: File not found or could not be opened.")
        return None

def CreateTableFromKey(key):
    key = key.upper()

    # Create a table from the key using the FairPlayTable module
    table = FairPlayTable.Table(key)

    return table.GetTable()

def CreateDiagraphs(plaintext):
    # Converts numbers to words
    plaintext = ConvertNumbersToWords(plaintext)

    # Remove punctuation and convert to lowercase
    plaintext = ''.join(filter(str.isalpha, plaintext))

    # Replace every occurence of "J" with "I"
    plaintext = plaintext.replace("j", "i").lower()

    diagraphs = []
    i = 0
    while i < len(plaintext):
        # Adds "z" to the end of the string if reached the end of the string
        if i == len(plaintext) - 1:
            diagraphs.append(plaintext[i] + "z")
            break

        # Appends the current letter and an "x" if the next letter is the same
        if plaintext[i] == plaintext[i + 1]:
            diagraphs.append(plaintext[i] + "x")
            i += 1

        # Appends the current and next letter to the list
        else:
            diagraphs.append(plaintext[i:i+2])
            i += 2

    return diagraphs

def ConvertNumbersToWords(text):
    # Converts numbers to words
    result = []
    words = text.split()
    for word in words:
        if word.isdigit():
            word = num2words(word)
        result.append(word)
    text = ' '.join(result)

    return text

def EncryptMessage(diagraphs, table):
    ciphertext = ""

    for diagraph in diagraphs:
        # Get the indices of the first letter
        row1, col1 = np.where(np.array(table) == diagraph[0].upper())
        row1 = row1[0]
        col1 = col1[0]

        # Get the indices of the second letter
        row2, col2 = np.where(np.array(table) == diagraph[1].upper())
        row2 = row2[0]
        col2 = col2[0]

        encryptedLetter1 = ""
        encryptedLetter2 = ""
        # Checks if the letters are in the same column
        if (col1 == col2):
            # Shift the letters down in the same column
            encryptedLetter1 = table[(row1 + 1) % 5][col1]
            encryptedLetter2 = table[(row2 + 1) % 5][col2]

        # Checks if the letters are in the same row
        elif (row1 == row2):
            # Shift the letters right in the same row
            encryptedLetter1 = table[row1][(col1 + 1) % 5]
            encryptedLetter2 = table[row2][(col2 + 1) % 5]

        # If the letters are not in the same row or column
        else:
            # Swap the letters in the rectangle
            encryptedLetter1 = table[row1][col2]
            encryptedLetter2 = table[row2][col1]
        
        ciphertext += encryptedLetter1 + encryptedLetter2

    return ciphertext.lower()

def OutputResults(key, ciphertext):
    file = open("ciphertext.txt", "w")
    file.write(key)
    file.write("\n" + ciphertext)
    file.close()



# Main function to run the encryption process
if (len(sys.argv) > 1):
    startTime = time.time()
    print("Starting encryption...")

    textfile = sys.argv[1]
    (key, plaintext) = GetDataFromFile(textfile)
    table = CreateTableFromKey(key)
    diagraphs = CreateDiagraphs(plaintext)
    ciphertext = EncryptMessage(diagraphs, table)
    OutputResults(key, ciphertext)

    exTime = math.floor((time.time() - startTime) * 1000)
    print("Message encrypted successfully!")
    print("Execution Time: " + str(exTime) + "ms")

else:
    print("ERROR: No file name provided!!!")