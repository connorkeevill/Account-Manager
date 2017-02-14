#CK

from Account import Account
from FileHandler import FileHandler
import templates, helpers

file = FileHandler('accounts.txt')

print(templates.greeting())

# |-------------------------------------------
# | Main loop for the program while running.
# |--------------------------------------
while True:
    file.getAccounts()
    choice = helpers.inputOption(templates.mainMenu(), ['A', 'V'])

    if choice == 'V':
        for account in file.accounts:
            templates.accountDetails(account.type, account.owner, account. username)

    elif choice == 'A':
        # |------------------------------------------
        # | Getting the details of the new account.
        # |--------------------------------------
        type = input('Enter the type of account this is: ')
        owner = input('Enter the name of the owner of the account: ')
        username = input('Enter the username of the account: ')
        password = input('Enter the account\'s password: ')
        key = input('!!IMPORTANT!! Enter the key that the password will be encrypted with:')
        account = Account(1, type, owner, username, password)
        account.encrypt(key)

        file.addAccount(account)