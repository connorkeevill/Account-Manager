#CK

import helpers
from objects.Account import Account
from recources import templates

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

        self.mainMenu()

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

    # | addAccount()
    # |----------------------------------------------------------------
    # | Takes details of the user's new account, makes the new account
    # | object and then uses the FileHandler object's method to add
    # | the new account object to the file in the correct format.
    # |--------------------------------------------------------
    def addAccount(self):  # TO be improved ---
        type = input('Enter the type of account this is: ')
        owner = input('Enter the name of the owner of the account: ')
        username = input('Enter the username of the account: ')
        password = input('Enter the account\'s password: ')
        key = input('!!IMPORTANT!! Enter the key that the password will be encrypted with:')
        account = Account(1, type, owner, username, password)
        account.encrypt(key)

        self.file.addAccount(account)
        self.mainMenu()

    # | viewAccounts()
    # |---------------------------------------------------------------------
    # | Prints all accounts and then allows the user to select an account
    # | to get it's password, or just to return to the main menu page.
    # |-----------------------------------------------------------
    def viewAccounts(self): # TO be improved ---
        self.file.getAccounts()
        self.printAccounts(self.file.accounts)

        selectAccount = helpers.inputOption('Do you wish to select an account? (Y/N)', ['Y', 'N'])

        if selectAccount == 'Y':
            account = self.file.accounts[self.getAccountIndex()]
            templates.accountDetails(account.type, account.owner, account.username, '=')
            keyword = self.getKeyword()
            account.decrypt(keyword)
            self.displayPassword(account.password)

        self.mainMenu()

    # | quit()
    # |--------------------------------------------------------
    # | Is called to close the program and destroy the object.
    # |-----------------------------------------------------
    def quit(self):
        None

    # | getAccountIndex()
    # |-----------------------------------------
    # | Gets the index of the account that the
    # | user is wanting to view details of.
    # |---------------------------------
    def getAccountIndex(self):
        numbers = self.getNumberRange()

        account = helpers.inputOption("Enter the index of the account you want: ", numbers)
        return int(account) - 1

    # | getKeyword()
    # |--------------------------------------------------------------------
    # | Gets the keyword for the account, and validates it with the user.
    # |----------------------------------------------------------------
    def getKeyword(self):
        sure = 'N'
        while sure == 'N':
            keyword = input("What's the keyword for this account?")
            sure = helpers.inputOption("Are you sure '" + keyword + "' is the correct keyword for this account? Y/N", ["Y", "N"])

        return keyword

    # | getNumberRange()
    # |-----------------------------------------------------
    # | Returns a list of numbers as strings based to be
    # | used when calling inputOption() as the options
    # | parameter. Bases list on the range of the
    # | accounts which are in the opened file.
    # |------------------------------------
    def getNumberRange(self):
        numbers = list(range(len(self.file.accounts) + 1))
        # |-------------------------------------------------------
        # | Gets rid of the first item as indexes start counting
        # | from zero and here the accounts are counted from
        # | one instead, to make it easier to read for the user.
        # |---------------------------------------------
        numbers.pop(0)
        strNumbers = []

        for number in numbers:
            strNumbers.append(str(number))

        return strNumbers

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

    # | displayPassword()
    # |---------------------------------------------
    # | Shows the user the password of the account,
    # | after it has been selected and decrypted.
    # |---------------------------------------
    def displayPassword(self, password):
        print('The password for this account is: ', password)

