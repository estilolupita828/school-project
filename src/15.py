def greet_user(name):
    """
    A simple function to greet the user.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

# Example usage:
user_name = "Alice"
greeting = greet_user(user_name)
print(greeting)
