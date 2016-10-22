#CK

from Password import Password
from fileHandler import fileHandler

word = input('Enter your password: ')
password = Password(1, word)
file = fileHandler()
password.encrypt('key')
file.addWrite(password.encrypted + "\n")
