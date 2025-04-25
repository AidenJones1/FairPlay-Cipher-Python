# Fair Play Cipher
#### Description: Separate Python files responsible for handling the encryption and decryption process using FairPlay Cipher

### About
Utilizes FairPlay Cipher to encrypt and decrypt messages

### How it works
This project consists of three Python files:
- FairplayCipherEncryption.py
- FairplayCipherDecryption.py
- FairPlayTable.py

And three example texts:
- example.txt (plaintext)
- ciphertext.txt (text after encryption)
- decipheredtext.txt (text after decryption)

#### Plaintext & Ciphertext .txt format
NOTE: The text should be formatted as such:
- The key MUST be on line 1 in the text file
- The key MUST contain only one word
- The message to be encrypted/deciphered MUST be in a line after line 1 (can be in one line or multiple lines)
- Since the FairPlay Cipher utilizes diagraphs (two-letter pairs), the ciphertext message MUST be even in length 

#### FairplayCipherEncryption.py
Responsible for encrypting a specific message and outputting the encrypted message as a file named `ciphertext.txt`. To use the file, enter the following prompt into the terminal: "python .\FairplayCipherEncryption.py {textFile}"

#### FairplayCipherDecryption.py
Responsible for decrypting a specific message and outputting a *rough* deciphered message as a file named `decipheredtext.txt`. To use the file, enter the following prompt into the terminal: "python .\FairplayCipherDecryption.py {textFile}"

#### FairPlayTable.py
Responsible for constructing a 5x5 table given a key

### How FairPlay Cipher Works (Encryption)
1. Create a table from the keyword.
2. Create a list of diagraphs from the plaintext.
3. Encrypt the diagraphs using the table.
4. Combine the encrypted diagraphs to form the ciphertext.
5. Output the key used and the ciphertext.

### How FairPlay Cipher Works (Decryption)
1. Create a table from the keyword.
2. Create a list of diagraphs from the ciphertext.
3. Decrypt the diagraphs using the table.
4. Combine the dectrypted diagraphs to form the decryptedtext.
5. Output the key used and the deciphered text.
