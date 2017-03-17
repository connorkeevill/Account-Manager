#CK

import templates, helpers
from Account import Account

# | CommandLine()
# |----------------------------------------------------------------------------
# | Class to handle all IO with the user. Will be instantiated to essentially
# | start the program. mainMenu() will be the 'homepage' and will call all
# | periphery methods to it, which will call mainMenu() once they have
# | ran. Only attribute needed is the file in use in that session.
# |------------------------------------------------------------

class CommandLine():
    def __init__(self, file):
        self.file = file

        self.greet()
        self.mainMenu()

    # | greet()
    # |---------------------------------------------
    # | Displays message shown on opening program.
    # |-----------------------------------------
    def greet(self):
        print(templates.greeting())

    # | mainMenu()
    # |-------------------------------------------------------------------------------
    # | The homepage which all periphery methods will return to (apart from quit()).
    # |--------------------------------------------------------------------------
    def mainMenu(self):
        choice = helpers.inputOption(templates.mainMenu(), ['A', 'V', 'Q'])

        if choice == 'A':
            self.addAccount()
        elif choice == 'V':
            self.viewAccounts()
        elif choice == 'Q':
            self.quit()

    def addAccount(self): # TO be improved ---
        type = input('Enter the type of account this is: ')
        owner = input('Enter the name of the owner of the account: ')
        username = input('Enter the username of the account: ')
        password = input('Enter the account\'s password: ')
        key = input('!!IMPORTANT!! Enter the key that the password will be encrypted with:')
        account = Account(1, type, owner, username, password)
        account.encrypt(key)

        self.file.addAccount(account)

    def viewAccounts(self):
        None

    def quit(self):
        None
