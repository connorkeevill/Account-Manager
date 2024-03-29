# CK

# | Note:
# |-------------------------------------------------------------------------------
# | The convention for the templates in this file will be that they are methods
# | which return a set message, which will then be printed. However when the
# | method takes parameters to make more 'personalised' message, then it
# | will be printed directly from the method as returning it causes a
# | problem with the messages formatting. Printing it fixes this,
# | preventing any kind of excessively complex implementation.
# |-------------------------------------------------------

# | greeting()
# |-----------------------------------------------------------
# | Returns message to be shown on the program being opened.
# |-------------------------------------------------------
def greeting():
	return ('===================================================================\n'
			'Welcome...\n'
			'===================================================================\n')


# | mainMenu()
# |-------------------------------------------------------------------------
# | Returns message to prompt user on choice for next action in main menu.
# |--------------------------------------------------------------------
def mainMenu():
	return ('Please select one of the following:\n'
			'- [A]dd a new account\n'
			'- [V]iew existing accounts\n'
			'- [Q]uit\n')


# | accountDetails()
# |---------------------------------------------------------------------------------
# | Template to show structured layout of 'non-confidential' details of an account.
# |-----------------------------------------------------------------------------
def accountDetails(type, owner, username, accountNum="="):
	print('=', accountNum, '===============================================================\n',
		  type, '-', owner, '\n',
		  '-----------------------------------------------------------------\n',
		  'Username:', username, '\n'
								 '===================================================================\n', )


# | setup()
# |---------------------------------------------------------------------
# | The introduction shown when the user is about to setup everything.
# |-----------------------------------------------------------------
def setup():
	return ('-----------------------------------------------------------------------------------\n'
			'Looks like this is the first time being here. Enter a few details to get started.\n'
			'-----------------------------------------------------------------------------------\n')
