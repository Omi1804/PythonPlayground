# Recursion --> when a function calls itself repeatedly

# Example: Print numbers from n to 1 backwards using recursion
def show(n):
    if n <= 0:  # Base case: If n is less than or equal to 0, stop the recursion.
        return
    print(n)  # Print the current value of n.
    show(n - 1)  # Recursive call: Call the show function with n-1.

show(10)  # Outputs: 10 9 8 7 6 5 4 3 2 1

# Factorial through recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case: If n is 0 or 1, return 1 (0! = 1 and 1! = 1).
        return 1
    return n * factorial(n - 1)  # Recursive call: Multiply n by the factorial of n-1.

print(factorial(5))  # Outputs: 120 (5! = 5*4*3*2*1)
