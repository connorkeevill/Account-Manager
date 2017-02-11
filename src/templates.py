#CK

# | displayGreeting()
# |------------------------------------------------------------
# | Displays message to be shown on the program being opened.
# |--------------------------------------------------------
def displayGreeting():
    print('Welcome') #(to be improved)

# | displayAccountDetails()
# |---------------------------------------------------------------------------------
# | Template to show structured layout of 'non-confidential' details of an account.
# |-----------------------------------------------------------------------------
def displayAccountDetails(type, owner, username):
    print('===================================================================\n',
          type,'-', owner, '\n',
          '-----------------------------------------------------------------\n',
          'Username:', username, '\n'
          '===================================================================\n',)
