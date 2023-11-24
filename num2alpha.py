#!/bin/python
# Remove the above line if the script fails to load, especially in
# Windows operating systems
# ---
# This program converts a non-zero positive integer into its mapping
# in the alphabetical form; and vice-versa

# The variables 'd', 'e', and 'f' in this script are thought to be the
# "variable conventions" used as a catch-all for a function's argument

import math
import argparse

# Parse the input prompt from user
parser = argparse.ArgumentParser(
    description='Converts natural number into alphabet, and vice versa')
parser.add_argument('prompt', metavar='N', type=str,
    help='The input natural number or alphabet set to convert from/to' +
    ' (autodetect)')
args = parser.parse_args()

# Let's store the user prompt in some nice string variable
pr = args.prompt

# Script-specific variable name reassignment
n = args.prompt

# ----------------------- FUNCTION DECLARATION ----------------------- #

alpha_list = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]

def alpha_to_number(d):
    '''
    This function converts any letter-digit of alphabet into its
    non-zero positive integer representation in base-10
    
    Returns an integer
    '''
    
    # Fail-safe; in case user got the string input mad
    d = d.lower()
    
    return alpha_list.index(d) + 1  # --- array starts at zero!

def number_to_alpha(d):
    '''
    This function converts a positive integer of range 1-26 into its
    respective alphabet correspondence
    
    Returns a string
    '''
    
    return alpha_list[d-1]

# -------------------------------------------------------------------- #

# Determining if the input argument is an integer or string
# Then decides which code block to call upon

if n.isalpha():
    # Let us parse letter-digit into natural number!
    
    # The length of the string
    i = len(n)
    
    # Create the reversed array of the input letter-digit string
    a = list(n)
    a.reverse()
    
    # Where the sum of all letter-digits' value is stored
    j = 0
    
    # Let's loop 'em!
    # Each letter-digit ordinal carries different weight, exponential
    # in size; we start from the leftmost (i.e., the biggest ordinal)
    # All of this operation is just multiplication, exponential power,
    # and addition!
    while i > 0:
        # Find out what natural number does this letter-digit represent
        k = alpha_to_number(a[i-1])  # --- dammit, array starts at zero!
        
        # Then perform exponential power, multiplication, and finally
        # addition/sum into variable 'j'
        j += k * 26**(i-1)
        
        # Now let's decrement the iterator integer
        i -= 1
    
    # Finally, let us present the result of alphabet-to-integer parsing!
    print(f'''
You asked for the base-10 integer representation of : {n}
Here's what you got{' '*33}: {j}
    '''.strip()
    )
    
elif n.isnumeric():
    # Let us convert from integer to letter-digit!
    
    # The power factor of the base number "26"
    # Used to determine the number of letter digit
    # i.e., "lowest_upper_bound" = number of letter digit
    lowest_upper_bound = 1
    
    # Keep dividing the input number by 26 until
    # it gets smaller than 26, while adding the value of variable
    # "lowest_upper_bound" by one on each iteration
    i = int(n)
    while i > 26:
        i /= 26
        lowest_upper_bound += 1
    
    # Now, here's how we rudimentarily determine each letter-digit's
    # alphabet correspondence:
    # 1. Start from the leftmost/biggest letter-digit (e.g., "1" in
    #    "1402"; this sample number have three letter-digits)
    # 2. Floor-divide the whole number by 26 to the power of the
    #    leftmost letter-digit ordinal minus one (in this case of the
    #    four-digit number "1402", "2" is the letter-digit ordinal after
    #    substraction); The number that pops out after floor-division
    #    is the letter-digit's alphabet correspondence
    # 3. Shift to the next right letter-digit (e.g., "4" in "1402")
    # 4. Substract current whole number by value obtained from step 2
    #    (in case of the third letter-digit of "1402", substract
    #    by "1152" because 1402 - (2 * 26^2) is equal to 1152)
    # 5. Repeat steps 2-4 ad infinitum to the next right letter-digit
    
    # Let's create an array with the size corresponding to the value
    # of the variable "lowest_upper_bound"
    a = [None] * lowest_upper_bound
    
    # Start from the leftmost/biggest letter-digit order
    # Substracted value of current whole number will be stored in "i"
    # The letter-digit's alphabet correspondence value will be stored in
    # array "a" as a string, rather than raw integer
    i = int(n)
    j = int(lowest_upper_bound)
    while j > 0:
        # Floor-divide the current whole number ('i')
        # by 26 to the power of 'j-1'
        # Then find its alphabet correspondence and store into array "a"
        floor_division_result = math.floor(i / 26**(j-1))
        l = number_to_alpha(floor_division_result)
        a[j-1] = l  # --- array must start at zero!
        
        # Update the current whole number value as per substraction
        # with this letter-digit's geometric/exponential value
        # Then store this current whole number value into array "a"
        i -= floor_division_result * 26**(j-1)
        
        # Decrement the loop iterator variable
        j -= 1
    
    # Reverse the content of the digit-letter array "a" because
    # the biggest digit-letter ordinal comes up first
    a.reverse()
    
    # Finally, let us present the alphabetical representation!
    print(f'''
You asked for the alphabetical representation of the number : {n}
Here's your letter-digits{' '*35}: {''.join(a)}
    '''.strip()
    )

else:
    print('You gotta be kidding! Pure strings xor integers only!')

# Bye-bye!
exit()
