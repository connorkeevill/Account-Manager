#CK

import templates, helpers, time
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

    def addAccount(self):  # TO be improved ---
        type = input('Enter the type of account this is: ')
        owner = input('Enter the name of the owner of the account: ')
        username = input('Enter the username of the account: ')
        password = input('Enter the account\'s password: ')
        key = input('!!IMPORTANT!! Enter the key that the password will be encrypted with:')
        account = Account(1, type, owner, username, password)
        account.encrypt(key)

        self.file.addAccount(account)

    def viewAccounts(self):
        self.file.getAccounts()
        self.printAccounts(self.file.accounts)

        selectAccount = helpers.inputOption('Do you wish to select an account? (Y/N)', ['Y', 'N'])

        if selectAccount == 'Y':
            self.selectAccount()
            #Add code for getting account password
        elif selectAccount == 'N':
            self.mainMenu()
        else:
            raise ValueError

    def quit(self):
        None

    def selectAccount(self):
        None

    # | printAccounts()
    # |----------------------------------------------------------------
    # | Prints all the accounts when the user selects the 'V' option.
    # | Uses the template in the templates in the file to show the
    # | accounts and also determines the account's index, so the
    # | user can select one after they've all been displayed.
    # |----------------------------------------------------
    def printAccounts(self, accounts):
        for account in range(len(accounts)):
            # |----------------------------------------
            # | Get index to be displayed on account.
            # |-----------------------------------
            index = account + 1

            templates.accountDetails(accounts[account].type, accounts[account].owner, accounts[account].username, index)
