#CK

# | greeting()
# |-----------------------------------------------------------
# | Returns message to be shown on the program being opened.
# |-------------------------------------------------------
def greeting():
    return('===================================================================\n'
          'Welcome\n'
          '===================================================================\n')

# | mainMenu()
# |-------------------------------------------------------------------------
# | Returns message to prompt user on choice for next action in main menu.
# |--------------------------------------------------------------------
def mainMenu():
    return('Please select one of the following:\n'
           '- [A]dd a new account\n'
           '- [V]iew existing accounts\n')

# | accountDetails()
# |---------------------------------------------------------------------------------
# | Template to show structured layout of 'non-confidential' details of an account.
# |-----------------------------------------------------------------------------
def accountDetails(type, owner, username):
    print('===================================================================\n',
          type,'-', owner, '\n',
          '-----------------------------------------------------------------\n',
          'Username:', username, '\n'
          '===================================================================\n',)
