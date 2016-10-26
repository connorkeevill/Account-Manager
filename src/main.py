#CK

from Account import Account
from FileHandler import FileHandler

file = FileHandler()

decision = input('Do you want to [V]iew existing accounts or [A]dd a new one? ').upper()

if decision == 'V':
    for account in file.accounts:
        print(account.type)
        account.decrypt('!')
elif decision == 'A':
    account = Account(1, 'account4', 'username4', 'password')
    account.encrypt('!')
    file.addAccount(account)
else:
    print('Invalid choice, exiting')