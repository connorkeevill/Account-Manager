#CK

# | Note:
# |-----------------------------------------------------------
# | This file will 'command' the running of the program. It
# | creates the command line and will ensure that the file
# | and all other dependencies are acquired before being
# | ran. The CommandLine() class makes this file more
# | clean, to make it just what initiates the rest.
# |--------------------------------------------

from FileHandler import FileHandler
from interface import CommandLine

file = FileHandler('accounts.txt')
console = CommandLine(file)
