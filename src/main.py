#CK

from Account import Account
from FileHandler import FileHandler
import templates

file = FileHandler('accounts.txt')

for account in file.accounts:
    templates.displayAccountDetails(account.type, account.owner, account. username)


