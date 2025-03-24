def print_pattern(n):
    """
    Print a pattern of numbers with n rows.
    
    Example:
    >>> print_pattern(1)
    *
    ***
   *****
  *******
 **********
"""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive integer and odd")

    for i in range(n):
        # Print the current row
        for j in range(i + 1):
            print(j, end="")
        
        # Add an empty line between rows
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    try:
        print_pattern(n)
    except ValueError as e:
        print(e)
