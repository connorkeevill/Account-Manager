#CK

# | inputOption()
# |--------------------------------------------------------------------------
# | Returns a character based on the input from the prompt if it is in the
# | options[] param. To be used to get the right input when getting the
# | user to make a choice from multiple options. The characters in
# | list passed for options NEED to be uppercase for them to be
# | recognised when compared to the user's inputted choice.
# |----------------------------------------------------
def inputOption(prompt, options):
    option = input(prompt)
    while option.upper() not in options:
        print('Make sure your choice is one of: ', ', '.join(options))
        option = input(prompt)

    return option