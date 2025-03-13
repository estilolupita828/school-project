from random import randint
def generate_random_python_code():
    # Generate a random number of lines
    num_lines = randint(10, 20)

    # Generate a list of random variables
    variables = []
    for i in range(num_lines):
        variables.append("var{}".format(i))

    # Generate a list of random statements
    statements = []
    for var in variables:
        statements.append("{}=randint(0, 100)".format(var))

    # Generate the code
    code = "\n".join(statements)
    return code