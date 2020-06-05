# CK

from configparser import ConfigParser

from recources import templates

configFilePath = '../data/config.ini'


# | getSettings()
# |----------------------------------------------------------
# | Gets the settings from the config file and returns them
# | in an array. Also will pass onto the setup() method
# | if the user hasn't ran the program before (i.e,
# | the config file has no relevant data in it).
# |-------------------------------------------
def getSettings():
	config = ConfigParser()
	config.read(configFilePath)

	# | If the user hasn't used the program before
	if config.getboolean('setup', 'firstRun'):
		print('setup')
		setup(config)

	user = config.get('user', 'name')
	keyword = config.get('data', 'keyword')
	filepath = config.get('data', 'filePath')

	return [user, keyword, filepath]


# | setup()
# |--------------------------------------------------------
# | Sets up the program to run for the user by populating
# | values in config.ini with inputted data. This will
# | only ever be run once, as the firstRun attribute
# | will be changed to indicate that it it setup.
# |-------------------------------------------
def setup(configFile):
	print(templates.setup())

	# |-----------------------------------------------------------------------
	# | For now I'll assume the user inputs valid data that won't need to be
	# | edited, however this will be changed once functionality is there.
	# |---------------------------------------------------------------

	# | Get user's details
	name = input('What\'s your name? ')
	keyword = input('What keyword do you want to use to encrypt and decrypt all your accounts? ')
	filepath = input("What's the filepath to the file which will contain the accounts? ")

	# | Prepare file
	file = open(configFilePath, 'w')

	print(configFile.sections())

	# | Write all details to file
	configFile.set('setup', 'firstRun', 'False')
	configFile.set('user', 'name', name)
	configFile.set('data', 'keyword', keyword)
	configFile.set('data', 'filepath', filepath)
	configFile.write(file)
	file.close()
