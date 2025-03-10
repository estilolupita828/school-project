import random

def get_random_number(n):
    return random.randint(1, n)

def get_random_word(words):
    return random.choice(words)

def get_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
