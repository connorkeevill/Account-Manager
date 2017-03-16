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

# | printAccounts()
# |----------------------------------------------------------------
# | Prints all the accoutns when the user selects the 'V' option.
# | Uses the template in the templates in the file to show the
# | accounts, and also displays the account's index, so the
# | user can select one after they've all been displayed.
# |----------------------------------------------------
def printAccounts(accounts):
    limit = 5

    for account in range(len(accounts)):
        # |----------------------------------------
        # | Get index to be displayed on account.
        # |-----------------------------------
        index = account + 1

        templates.accountDetails(accounts[account].type, accounts[account].owner, accounts[account].username, index)
        time.sleep(0.1)

# | selectAccount()
# |-----------------------------------------
# | Gets the index of the account that the
# | user is wanting to view details of.
# |---------------------------------
def selectAccount(accounts):
    numbers = getNumberRange(accounts)

    account = inputOption("Enter the index of the account you want: ", numbers)
    return int(account) - 1

# | getNumberRange()
# |-----------------------------------------------------
# | Returns a list of numbers as strings based to be
# | used when calling inputOption() as the options
# | parameter. Bases list on the range of the
# | accounts which are in the opened file.
# |------------------------------------
def getNumberRange(accounts):
    numbers = list(range(len(accounts) + 1))
    # |-------------------------------------------------------
    # | Gets rid of the first item as indexes start counting
    # | from zero and here the accounts are counted from
    # | one instead, to make it easier to read for the user.
    # |---------------------------------------------
    numbers.pop(0)
    strNumbers = []

    for number in numbers:
        strNumbers.append(str(number))

    return strNumbers

