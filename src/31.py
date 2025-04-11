def sum_of_squares(numbers):
    """
    Calculate the sum of squares of given numbers

    Parameters:
    numbers (list): A list of integers or floats

    Returns:
    float: Sum of squares of the input numbers
    """
    return sum(x ** 2 for x in numbers)

# Example usage
numbers = [1, 2, 3]
print(sum_of_squares(numbers))  # Output: 14
