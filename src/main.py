#CK

from Account import Account
from fileHandler import fileHandler

word = input('Enter your password: ')
account = Account(1, word)
file = fileHandler()
account.encrypt('key')
file.append(account.encrypted + "\n")
