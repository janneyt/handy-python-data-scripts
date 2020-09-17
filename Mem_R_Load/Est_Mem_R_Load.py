import sys


IS_VALID = ["-h","-o","-e","-8n","-idk","-c","-4i"]
MSG_VALID = ("\n\nThe valid options for this program are:\n\t-h (help)"
               +"\n\t-o (valid options)\n\t-e (exit)\n\t-8n for 8 byte numeric"
               +"data\n\t-4i for 4 byte integer data\n\t-c for characters\n\t-idk"
               +"if you need help selecting a datatype\n")
MSG_INT_INVALID = ("\n\nPlease only select a valid integer as listed above,"
                     +" without periods, letters or any other character.\n")
ALL_INVALID = ("\n\nYou have selected in invalid option.\nPlease select a valid"
                 +"option.\nIf you do not know the valid options, press -o and"
                 +"one will be assigned to you.\n")
INITIAL_MSG = ("\n\nPlease identify the largest data type for the file.\nPress"
                 +"-h for help, -o to see valid options, -e to exit.\n")
SCFL_CALC_MSG = ("\n\nWould you like to run another calculation (Y),"
                 +"or press -e to exit.\n")

NOT_A_STRING = ("\n\nYou attempted a command line argument that was not a string. "
                +"\nPlease enter a character of the alphabet (A-Z, a-z)"
                +"\npreceded by a dash (-).\n")

NOT_AN_INT = ("\n\nYou attempted a command line argument that was not an int."
             +"\nPlease enter a sequence of integers between 0 and "
             + str(sys.maxsize)+"\n")

ESCAPE_SEQUENCES = ['\\x07',"'",'"','\\\\',"\\'",'\\x08','\\x0c','\\n','\\r','\\t']

'''
################################################################################
Input Functions
################################################################################
'''

def get_input(nxt_input):
    '''
    Gets input from the user and makes sure it is valid.

    Is this functional? The input is a string, theoretically. It does not mutate
    in any way through this function, and is in turn passed to another function.

    The only actual way to exit the function is through the evaluate_for_options
    function. This is entered through a "true" evaluation in the if/else control
    statement. The else clause just calls get_input after soliciting input.

    This is not a recursive function per se, although the else statement looks
    recursive.

    Raises an exception if someone tries to pass input that isn't a string.
    If the str() function succeeds it *Technically* violates functional programming.

    Restrictions on use: requires string input preceded by a dash. Not suitable
    for other types of input.

    '''
    try:
        str(nxt_input)
        if nxt_input in IS_VALID:
            evaluate_for_options(nxt_input)
        else:
            print(ALL_INVALID)
            command = input(MSG_VALID)
            get_input(command)
    except Exception as e:
        print(e)
        print(NOT_A_STRING)
        command = input(MSG_VALID)
        get_input(command)

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
    spaces_input = init_input.strip()
    raw_input = repr(spaces_input)
    return recursive_remove_escape(raw_input, ESCAPE_SEQUENCES[0])



def recursive_remove_escape(func_input, esc_seq):
    '''
    Removes escape characters from an input.
    '''


    if esc_seq == None:
        return func_input
    elif func_input:
        if esc_seq in ESCAPE_SEQUENCES:
            counter = ESCAPE_SEQUENCES.index(esc_seq)
            if esc_seq != ESCAPE_SEQUENCES[-1]:
                print("unstripped output", func_input)
                stripped_output = func_input.strip(esc_seq)
                print("stripped output", stripped_output)
                return recursive_remove_escape(stripped_output, ESCAPE_SEQUENCES[counter+1] )
            elif esc_seq == ESCAPE_SEQUENCES[-1]:
                stripped_output = func_input.strip(esc_seq)
                return recursive_remove_escape(stripped_output, None)
        elif esc_seq not in ESCAPE_SEQUENCES:
            return recursive_remove_escape(func_input, ESCAPE_SEQUENCES[0])
    else:
        if func_input:
            recursive_remove_escape(func_input, None)
        else:
            print("Something is really messed up, func_input somehow is none")

'''
################################################################################
Exit Functions
################################################################################
'''

def evaluate_for_exit():
    '''
    Confirms user really wants to exit program, then exits or not as appropriate.

    There is no global state interacted with at all in this function. It is
    merely a confirmation of exit. Again, the functional nature of testing the
    input is disputable, but I don't really see a way to do it otherwise.

    Exceptions should be raised if a string is not passed as input.

    This function automatically brings up the options menu on all inputs except
    a confirmation of exit. So, it should only be used with that in mind.
    '''
    response = input("\nDo you want to exit this program? Y/n\n")
    type(response)
    try:
        str(response)
        if response == "Y":
            sys.exit()
        elif response == 'n':
            get_input("-o")
        else:
            get_input("-o")
    except Exception as e:
        print(e)
        print(NOT_A_STRING)
        evaluate_for_exit()

def query_exit():
    '''
    Queries if user wants to calculate the size of other files, or to exit.

    This is another exit function, used after a successful calculation. As such,
    it is automatically functional since it doesn't interact with global state
    variables, or do anything other than evaluate input.

    Exceptions should be raised if input is not a string.

    This function should only be used upon successful completion of a task.
    '''
    response4 = input(SCFL_CALC_MSG)
    try:
        str(response4)
        if response4 == "Y":
            get_input("-o")
        elif response4 == "n":
            evaluate_for_exit()
        else:
            print(ALL_INVALID)
            query_exit()
    except Exception as e:
        print(e)
        print(ALL_INVALID)
        query_exit()

'''
################################################################################
Assistance Functions (Help Menu)
################################################################################
'''
def evaluate_for_char():
    '''
    Calculates the size of a string based on the size of a character being one
    byte.

    I'm assuming that the longest string is relatively easy to find. Further
    development would calculate this. Also, based on the R documentation, a
    character is stored as one byte. I need to verify this more rigorously since
    it would make an integer (4 bytes) larger than a character (1 byte).

    This is yet another function that doesn't really qualify as functional or
    imperative, it just takes some input, sanitizes it, and passes it to other
    functions.

    Exceptions should be raised if you enter a number other than a valid integer.
    Note that negative numbers are NOT allowed.

    This can be used to evaluate characters and pass the length of the longest
    string to other functions. It has very specific usage, probably not useful
    in other circumstances.
    '''
    print("\nThe data is probably characters, at 1 bytes per character value.\n")
    try:
        longest_character = input("\nWhat is the longest string in the dataset?\n")
        int(longest_character)
        calculate_approximate_memory(longest_character)
    except Exception as e:
        print(e)
        print(NOT_AN_INT)


def evaluate_for_options(nxt_input):
    '''
    Evaluates input and directs to appropriate function.

    I don't like switch statements usually. This could have been written as a
    switch but at least in python there isn't a large computational difference
    and I prefer the nomenclature (if, elif, else) rather than (case).

    Exception should be raised if nxt_input is not a string.

    This is the code representation of the help menu. It's not very abstract,
    so it shouldn't be used elsewhere.

    '''
    print(str(nxt_input))

    '''
    try:
        str(nxt_input)

        if nxt_input == "-h":
            evaluate_for_help()
        elif nxt_input == "-o":
            print(MSG_VALID)
            get_input("-o")
        elif nxt_input == '-e':
            evaluate_for_exit()
        elif nxt_input == '-8n':
            calculate_approximate_memory(8)
        elif nxt_input == '-idk':
            walkthrough_data_types()
        elif nxt_input == '-4i':
            calculate_approximate_memory(4)
        elif nxt_input == '-c':
            evaluate_for_char()
        else:
            print("\nNot a currently valid option, how did it get here?\n")
            print("\nDeficient input is: \n")
            print(nxt_input)
            command = input(ALL_INVALID)
            get_input(command)
    except Exception as e:
        print(e)
        print("\nThe help menu does not recognize the input sent to it.\n")
        print(NOT_A_STRING)
        evaluate_for_options("-o")
'''


def walkthrough_data_types():
    '''
    Helps the user decide what datatype is being used in the csv file.

    Note that there are two situations where the function calls itself. Both
    are meant to alert the user that they are entering invalid input.
    '''
    print("\nByte encoding information from:"
         +"https://www.stat.auckland.ac.nz/~paul/ItDT/HTML/node76.html")
    response1 = input("Is there a decimal place, a negative number, or anything"
                     +"else that coerces to a numeric?\nThis includes long"
                     +"integers and floats. Y/n\n")
    if response1 == 'Y':
        print("\nThe size of all data from your dataset is 8 bytes per entry."
             +"\nThis may be an overreaction but is a good upper bound.\n")
        print("\nStarting calculation with 8 bytes per entry\n")
        calculate_approximate_memory(8)
    elif response1 == 'n':
        response2 = input("Are there any numbers at all? Y/n")
        if response2 == 'Y':
            print("\nThe size of all data from your dataset is 4 bytes per"
                 +"entry.\nThis may be an overreaction but is a good upper bound.\n")
            calculate_approximate_memory(4)
        elif response2 == 'n':
            evaluate_for_char()
        else:
            print(ALL_INVALID)
            print("\n")
            walkthrough_data_types()
    else:
        print(ALL_INVALID)
        print("\n")
        walkthrough_data_types()


def evaluate_for_help():
    '''
    Evaluates input to help user to decide what type of help they need.
    '''
    nc = input("\n\nPlease select from the following options:"
              +"\n1. I'm not sure what command line option to use"
              +"\n2. I'm not sure what the biggest data type is\n")
    if nc == "1":
        evaluate_for_options("-o")
    elif nc == "2":
        walkthrough_data_types()
    else:
        print(MSG_INT_INVALID)
        get_input(INITIAL_MSG)


'''
################################################################################
Calculation Function (Help Menu)
################################################################################
'''

def calculate_approximate_memory(data_bytes):
    '''
    Performs the actual calculation of memory size.

    Basic mathematical calculation is rows in csv file, multiplied by columns in
    csv file, and finally result is multiplied by the input (number of bytes
    in data type).
    Input: an integer
    Outputs:

    '''
    rows = input("\nHow many rows are in the data file?\n")
    try:
        int_rows = int(rows)
    except:
        print("\nCannot convert to integer\n")
        rows = input(MSG_INT_INVALID)
    columns = input("\nHow many columns are in the data file?\n")
    try:
        int_columns = int(columns)

    except:
        print("\nCannot convert to integer\n")
        columns = input(MSG_INT_INVALID)
    try:
        int_data_bytes = int(data_bytes)
    except:
        print("\nSomehow the data size was passed as something other than a number.\nPlease enter again as a number 0-9 on the keyboard, and NOTHING ELSE.\n")
        calculate_approximate_memory(input())

    #This is the *actual* calculation.
    #Rule of thumb is the amount of memory needed to read in for R datasets is
    #twice the size of the dataset sitting in memory. So size doubles the calculation.
    size = (int_rows * int_columns * int(data_bytes))/(2**20)*2

    print("Your estimated R file size is: ",size," MB")
    query_exit()




command = input(INITIAL_MSG)
get_input(command)
