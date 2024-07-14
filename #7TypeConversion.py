# There are two types of conversions:
# Type Conversion and Type Casting 

# Type Conversion: Python automatically handles this.

a = 2  # 'a' is an integer.
b = 4.35  # 'b' is a float.

sum = a + b 
# Python automatically converts the integer 'a' to a float to perform the addition.
# The result is a float.

print(sum)  # Output will be 6.35


# Type Casting: We explicitly convert the value from one type to another.

c = int("1")  # The string "1" is explicitly converted to an integer.
d = 3.45  # 'd' is a float.

sum2 = c + d
# 'c' is an integer, and 'd' is a float. Python will convert 'c' to a float for the addition.
# The result is a float.

print(sum2)  # Output will be 4.45
