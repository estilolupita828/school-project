import random

def generate_random_code():
    """Generate a random string of 8 characters consisting only of letters and numbers."""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    code = ""
    for i in range(8):
        code += random.choice(alphabet)
    return code
