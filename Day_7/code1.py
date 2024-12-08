import itertools
import os

# Define a function to evaluate the expression with left-to-right evaluation
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '*':
            result *= numbers[i]
    return result

# Function to check if a given equation can be valid with operator combinations
def is_valid_equation(test_value, numbers):
    # Generate all possible combinations of operators (+, *)
    operator_combinations = itertools.product(['+', '*'], repeat=len(numbers) - 1)
    
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

# Function to solve the problem
def total_calibration_result(file_path):
    total = 0
    
    # Debugging: Check current working directory
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if the file exists before reading
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return 0
    
    # Open the input file and read each line
    with open(file_path, 'r') as file:
        equations = file.readlines()
    
    # Iterate over each equation in the input file
    for equation in equations:
        equation = equation.strip()  # Remove leading/trailing whitespace
        test_value, *numbers = equation.split(":")
        test_value = int(test_value)
        numbers = list(map(int, numbers[0].split()))
        
        # Check if the equation can be made valid
        if is_valid_equation(test_value, numbers):
            total += test_value
    
    return total

# File path to the input file
input_file_path = "input.txt"  # Ensure this path is correct

# Calculate the total calibration result
result = total_calibration_result(input_file_path)
print(f"Total calibration result: {result}")
