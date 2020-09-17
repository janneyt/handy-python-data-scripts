def strip_input(init_input):
    '''
    Looks for command line arguments and strips them into valid command.

    Inputs: any string input.
    Output: a series of string inputs, directed to evaluate_for_options().

    I created this function because there were issues with carriage returns ("\ r")
    messing up command line arguments. Although there should be some built-in
    support for this style of command line argument, I found it far too easy
    to include subtle bugs without some sort of stripping function.

    The function should take each argument passed to it (separated by "-")
    and create separate evaluations of each command. This means that there could
    be a large number of potential commands, and each one should be displayed
    and confirmed by the user.

    Example: say a user enters -h -idk. This should be evaluated as:
        1. bring up the help menu.
        2. bring up a confirmation window asking if the user wants to continue
           command '-idk'
        3. if the answer to 2 is yes, then bring up -idk.
        4. if the answer to 2 is no, return to usage screen.

    Since the above example requires commands to be strings, exceptions should be
    raised if it is not a string. Similarly, arguments need to be checked against
    IS_VALID and must also be checked for dashes (the separator). Spaces longer
    than one space should reset the function with an invalid input message
    directing user to use separator. Invalid arguments should be deleted, and all
    valid arguments performed, before asking if there is anything else the user
    wants to do.

    This function should be fine to use in any input stripping situation. I'm
    trying to make it abstract enough that you can use it for just about anything
    that you need carefully inputted.

    '''

    '''
    Strip off trailing controlling character.
    '''
    spaces_input = init_input.strip()
    raw_input = repr(spaces_input)
    stripped_input = raw_input.strip()
    no_quotes_input = stripped_input.strip("''")
    no_car_input = no_quotes_input.strip('\r')
    return no_car_input
