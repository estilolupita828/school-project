import random
def get_random_python_code():
    """Returns a random Python code"""
    code = ""
    while not code or " " in code or "\n" in code or "\t" in code:
        code = ''.join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(random.randint(1, 10)))
    return code