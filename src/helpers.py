#CK

import templates
import time

# | inputOption()
# |--------------------------------------------------------------------------
# | Returns a character based on the input from the prompt if it is in the
# | options[] param. To be used to get the right input when getting the
# | user to make a choice from multiple options. The characters in
# | list passed for options NEED to be uppercase for them to be
# | recognised when compared to the user's inputted choice.
# |----------------------------------------------------
def inputOption(prompt, options):
    option = getOption(prompt)
    while option not in options:
        print('Make sure your choice is one of: ', ', '.join(options))
        option = getOption(prompt)

    return option

# | getOption()
# |-------------------------------------------------------------------
# | Gets the option variable needed for inputOption(), to get it in
# | uppercase and strip the whitespace to get a single character.
# |----------------------------------------------------------
def getOption(prompt):
    option = input(prompt).upper()
    option.replace(" ", "")

    return option

def printAccounts(accounts):
    limit = 5

    for account in accounts:
        templates.accountDetails(account.type, account.owner, account.username)
        time.sleep(0.1)

