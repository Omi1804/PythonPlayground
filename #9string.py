# Escape sequence characters
# \n makes the string start from the next line 

str1 = "This is the string. \nwe are creating next line in python"
print(str1)
# Output:
# This is the string. 
# we are creating next line in python


# Operations on strings in Python

# Concatenation
a = "apna"
b = "college"
print(a + " " + b)  # The '+' operator concatenates strings with a space in between.
# Output: apna college

# Length of the string
print(len(a))  # The len() function returns the length of the string 'a'.
# Output: 4

# Getting a character in the string
ch = str1[2]
print(ch)  # Accessing the character at index 2 in 'str1'.
# Output: i


# Slicing: Accessing part of the string
strNew = "Apna_college"
print(strNew[1:4])  
# [1:4] means the slice starts from index 1 and goes up to, but does not include, index 4.
# Output: pna

print(strNew[3:])  
# Here it slices the string from index 3 to the end of the string.
# Output: a_college

print(strNew[-5:-1])  
# Negative indices mean slicing from the end of the string.
# -5 is the fifth last character and -1 is the last character (not included).
# Output: lleg
