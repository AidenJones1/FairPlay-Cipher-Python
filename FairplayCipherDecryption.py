# *Roughly* decrypts a message using a cipher based on the FairPlay table.

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
        ciphertext = " ".join(lines[1:]).strip()

        return (key, ciphertext)
    except:
        print("ERROR: File not found or could not be opened.")
        return None

def CreateTableFromKey(key):
    key = key.upper()

    # Create a table from the key using the FairPlayTable module
    table = FairPlayTable.Table(key)

    return table.GetTable() 

def CreateDiagraphs(ciphertext):
    diagraphs = []
    # Breaks the ciphertext into diagraphs of 2 letters each
    for i in range(0, len(ciphertext), 2):
        diagraphs.append(ciphertext[i:i + 2])

    return diagraphs

def DecryptMessage(diagraphs, table):
    decryptedText = ""

    for diagraph in diagraphs:
        # Get the indices of the first letter
        row1, col1 = np.where(np.array(table) == diagraph[0].upper())
        row1 = row1[0]
        col1 = col1[0]

        # Get the indices of the second letter
        row2, col2 = np.where(np.array(table) == diagraph[1].upper())
        row2 = row2[0]
        col2 = col2[0]
    
        decryptedLetter1 = ""
        decryptedLetter2 = ""
        # Checks if the letters are in the same column
        if (col1 == col2):
            # Shift the letters up in the same column
            decryptedLetter1 = table[(row1 + 4) % 5][col1]
            decryptedLetter2 = table[(row2 + 4) % 5][col2]

        # Checks if the letters are in the same row
        elif (row1 == row2):
            # Shift the letters left in the same row
            decryptedLetter1 = table[row1][(col1 + 4) % 5]
            decryptedLetter2 = table[row2][(col2 + 4) % 5]

        # If the letters are not in the same row or column
        else:
            # Swap the letters in the rectangle
            decryptedLetter1 = table[row1][col2]
            decryptedLetter2 = table[row2][col1]
        
        decryptedText += decryptedLetter1 + decryptedLetter2

    return decryptedText.lower()

def OutputResults(key, decryptedText):
    file = open("decipheredtext.txt", "w")
    file.write(key)
    file.write("\n" + decryptedText)
    file.close()



# Main function to run the decryption process
if (len(sys.argv) > 1):
    startTime = time.time()
    print("Starting decryption...")

    textfile = sys.argv[1]
    (key, ciphertext) = GetDataFromFile(textfile)
    table = CreateTableFromKey(key)
    diagraphs = CreateDiagraphs(ciphertext)
    decryptedText = DecryptMessage(diagraphs, table)
    OutputResults(key, decryptedText)

    exTime = math.floor((time.time() - startTime) * 1000)
    print("Message decrypted successfully!")
    print("Execution Time: " + str(exTime) + "ms")

else:
    print("ERROR: No file name provided!!!")