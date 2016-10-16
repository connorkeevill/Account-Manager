#CK
from Password import Password

word = input('Please enter the password you want to encrypt: ')
keyword = input('Please enter the keyword to use for encryption: ')
password = Password(1, word)

password.encrypt(keyword)