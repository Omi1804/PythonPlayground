# Functions are of two types:
# 1. Built-in functions: These are functions that are predefined in Python (e.g., print(), len(), etc.).
# 2. User-defined functions: These are functions that you create to perform specific tasks.

# You can check the parameters of built-in functions by hovering over them in most IDEs or by using the help() function.
# Example: print()

# Default parameters in functions
# Default parameters allow you to define default values for parameters in case no arguments are passed during the function call.
def cal_prod(a=1, b=1):  # If no arguments are passed, it will use the default values (a=1, b=1).
    return a * b

print(cal_prod(3, 4))  # Outputs: 12
print(cal_prod())      # Outputs: 1 (using default values)

# Write a program to find the factorial of n
def Fact_to_N(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i  # Multiply current fact by i for each iteration
    return fact

print(Fact_to_N(5))  # Outputs: 120 (5! = 5*4*3*2*1)
