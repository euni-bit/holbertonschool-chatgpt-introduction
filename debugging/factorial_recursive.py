#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Parameters:
    - n (int): The number whose factorial is to be calculated.

    Returns:
    - int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command line argument handling
if __name__ == "__main__":
    """
    The entry point of the script. Reads a number from the command line arguments,
    calculates its factorial using the factorial function, and prints the result.
    """
    f = factorial(int(sys.argv[1]))
    print(f)
