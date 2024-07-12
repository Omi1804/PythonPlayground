# Rule 1
a, b = 2, 3  # Assigning values 2 and 3 to variables a and b

Txt = "@"  # Assigning the string "@" to variable Txt

# This will print the "@" 2*3 times.
# The multiplication is evaluated left to right, so first 2*Txt gives "@@", then @@*3 gives "@@@@@@"
print(2 * Txt * 3) 

# Rule 2
A, B = "2", 3  # Assigning string "2" to A and integer 3 to B

Txt = "@"  # Assigning the string "@" to variable Txt
# Here, A and Txt will concatenate with the + sign.
# (A + Txt) gives "2@", then "2@"*B gives "2@2@2@"
print((A + Txt) * B)

# Rule 3
# Remainder is negative when the denominator is negative
D = -5  # Assigning value -5 to variable D
C = B % D  # Calculating the remainder when B (3) is divided by D (-5)
print(C)  # The remainder is -2

# Multi line comments
"""
Rules for calculating expressions
"""
