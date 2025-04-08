def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
try:
    print(calculate_average(numbers))
except ValueError as e:
    print(e)
