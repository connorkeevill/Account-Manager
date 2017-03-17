#CK





from Account import Account
from FileHandler import FileHandler
import templates, helpers
from interface import CommandLine

file = FileHandler('accounts.txt')
console = CommandLine(file)



# file = FileHandler('accounts.txt')
#
# print(templates.greeting())
#
# # |-------------------------------------------
# # | Main loop for the program while running.
# # |--------------------------------------
# while True:
#     choice = helpers.inputOption(templates.mainMenu(), ['A', 'V', 'Q'])
#
#     if choice == 'V':
#         file.getAccounts()
#         helpers.printAccounts(file.accounts)
#         selectedAccount = file.accounts[helpers.selectAccount(file.accounts)]
#
#         templates.accountDetails(selectedAccount.type, selectedAccount.owner, selectedAccount.username)
#         keyword = input("Enter the keyword used to this account: ")
#
#         selectedAccount.decrypt(keyword)
#         print("This account's password is: ", selectedAccount.password, "\n")
#
#     elif choice == 'A':
#         # |------------------------------------------
#         # | Getting the details of the new account.
#         # |--------------------------------------
#         type = input('Enter the type of account this is: ')
#         owner = input('Enter the name of the owner of the account: ')
#         username = input('Enter the username of the account: ')
#         password = input('Enter the account\'s password: ')
#         key = input('!!IMPORTANT!! Enter the key that the password will be encrypted with:')
#         account = Account(1, type, owner, username, password)
#         account.encrypt(key)
#
#         file.addAccount(account)
#
#     elif choice == 'Q':
#         break