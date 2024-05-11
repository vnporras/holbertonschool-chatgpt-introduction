#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given integer using recursion.

    Parameters:
    - n: Integer input for which factorial needs to be calculated.

    Returns:
    - Integer: Factorial of the input integer.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: factorial of n is n times factorial of (n-1)

f = factorial(int(sys.argv[1]))  # Calculate factorial using the input from the command line argument
print(f)  # Print the calculated factorial
