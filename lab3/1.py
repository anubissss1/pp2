class String:
    def __init__(self):
        self.S = ''

    def getString(self):
        self.S = input()
    
    def printString(self):
        print(self.S.upper())

S = String()
S.getString()
S.printString()
