import numpy as np

class Table:
    def __init__(self, key):
        self.table = []
        self.currentRow = []
        self.key = key
        self.GenerateTable()

    def GenerateTable(self):
        # Remove delicate letters from the key
        keyUnique = []
        for char in self.key:
            if char not in keyUnique:
                keyUnique.append(char)

        # Adds the keyword with unique letters to the table first
        for i in range(len(keyUnique)):
            Table.AddToCurrentRow(self, keyUnique[i])

        # Add the remaining alphabet letters to the table in order
        for i in range(65, 91):
            char = chr(i)

            # Checks if the letter is already in the table or if it is "J"
            if char in np.array(self.table) or char in self.currentRow or char == "J":
                continue

            Table.AddToCurrentRow(self, char)

    def AddToCurrentRow(self, char):
        self.currentRow.append(char)

        # Checks if the row is full (5)
        if len(self.currentRow) == 5:
            self.table.append(self.currentRow)
            self.currentRow = []
    
    def GetTable(self):
        return self.table

    def PrintTable(self):
        for row in self.table:
            print(row)
