import random

def get_random_string(length=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result
