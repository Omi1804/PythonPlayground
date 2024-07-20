# A block of statements that performs a specific task is known as a function.
# Functions help in organizing code, making it reusable and modular.

# Function definition syntax:
# def functionName(param1, param2):
#     # some work
#     return Value

# Example function to calculate the sum of two numbers
def calc_sum(a, b):
    return a + b

# Function call with arguments
print(calc_sum(1, 2))  # Outputs: 3

# A function that doesn't explicitly return a value returns None by default.

# Function to calculate the average of three numbers
def calc_avg(a, b, c):
    sum = a + b + c  # Calculate the sum of the three numbers
    avg = sum / 3  # Calculate the average
    print(avg)  # Print the average
    return avg  # Return the average

calc_avg(1, 2, 3)  # Outputs: 2.0
