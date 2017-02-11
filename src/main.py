#CK

from Account import Account
from FileHandler import FileHandler
import templates

file = FileHandler('accounts.txt')

#Insert code for selection of programs function:




#Displaying accounts w/out password
for account in file.accounts:
    templates.displayAccountDetails(account.type, account.owner, account. username)




