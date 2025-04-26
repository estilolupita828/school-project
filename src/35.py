import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Args:
        length (int): The desired length of the generated string.
        
    Returns:
        str: A randomly generated string of the given length.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage:
random_string = generate_random_string(10)
print("Random String:", random_string)
