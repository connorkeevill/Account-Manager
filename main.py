#CK
from Password import Password

word = input('Please enter the password you want to encrypt: ')
password = Password(1, word)

print(password.cases)