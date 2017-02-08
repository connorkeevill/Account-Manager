#CK

from Account import Account
from fileHandler import fileHandler

# | Currently a file to create a new account object with new data from the user
# | and write it to the passwords.txt file. Certain parameters are hard coded
# | for now to test specific aspects.

word = input('Enter your password: ')
account = Account(1, word)
file = fileHandler()
account.encrypt('key')
file.append(account.encrypted + "\n")
