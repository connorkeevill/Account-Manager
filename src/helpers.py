#CK

import hashlib

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

# | sha1_hash()
# |-----------------------------------------------------------------
# | Takes a string as input, and returns it's sha1 hash. Uses the
# | python module hashlib, and it's sha1 function. It also
# | converts the string into a byte object and returns
# | the hash as a hexadecimal string, with hashlib.
# |--------------------------------------------
def sha1_hash(string):
    byteString = bytes(string, 'utf-8')
    hashString = hashlib.sha1(byteString).hexdigest()
    print(hashString)
    return hashString