#CK

from Account import Account

# | fileHandler()
# |--------------------------------------------------------------------------------------
# | Object to handle any file IO. This is created as a wrapper for Python's file object
# | to bundle everything into an object which is easier to manage. The fileHandler()
# | object acts as a file which remains open, but actually operates by storing a
# | file name, and opening that file in the required mode every time data is
# | written or appended to it, or read from it. This allows methods like
# | file.add() to be used in parallel with functions like file.read()
# | without having to worry about closing and reopening the file
# | in a different mode, making it easier to interact with it.
# |-------------------------------------------------------
class FileHandler():
    def __init__(self, fileName=None):

        if fileName == None:
            self.fileName = self.getFileName()
        else:
            self.fileName = fileName

        self.file = None
        self.accounts = self.getAccounts()

    # | getFileName()
    # |-----------------------------------------------------
    # | If the object was initialised without a file name,
    # | this method prompts the user to enter one, and
    # | ensures that the entered directory is valid
    # | with a simple 'while, try, except' loop.
    # |-------------------------------------
    def getFileName(self):
        prompt = 'Please enter the directory of the file you\'re using: '

        while True:
            try:
                name = input(prompt)
                newFile = open(name)
                newFile.close()
                break
            except:
                print('FAILED')
                print('Make sure the file you\'re attempting to open exists and that you have the correct file path.')
        return name

    # | getAccounts()
    # |-----------------------------------------------------
    # | Returns a list contain Account() objects that have
    # | been created using details fromm a test file.
    # |-----------------------------------------
    def getAccounts(self):
        self.file = open(self.fileName, 'r')
        accounts = []

        for line in self.file:
            details = line.split(', ')
            account = Account(0, details[0], details[1], details[2][:-1])
            accounts.append(account)

        self.file.close()
        return accounts

    # | addAccount()
    # |------------------------------------------------------------
    # | Writes a new account entry to the file by extracting data
    # | from an Account() object and writing it to the file.
    # |-------------------------------------------------
    def addAccount(self, account):
        self.file = open(self.fileName, 'a')
        details = [account.type, account.username, account.encrypted]
        line = ", ".join(details)

        self.file.write(line + '\n')
        self.file.close()

"""
    # | append()
    # |-----------------------------------------------
    # | Assumes there is no file open and opens the
    # | file in 'a' mode, then calls the class'
    # | write method with the message param.
    # |---------------------------------
    def append(self, message):
        self.file = open(self.fileName, 'a')
        self.write(message)

    # | overWrite()
    # |-----------------------------------------------
    # | Assumes there is no file open and opens the
    # | file in 'w' mode, then calls the class'
    # | write method with the message param.
    # |---------------------------------
    def overWrite(self, message):
        self.file = open(self.fileName, 'w')
        self.write(message)

    # | write()
    # |-----------------------------------------------
    # | Assumes there is a file open, and calls the
    # | file's write() method using the message
    # | parameter, before closing the file.
    # |--------------------------------
    def write(self, message):
        self.file.write(message)
        self.file.close()

"""