# More Functions in Strings

str = "I am A Coder In Hell"

print(str.endswith("ell"))  
# Checks if the string ends with the substring "ell".
# Output: True

print(str.capitalize())  
# Capitalizes the first character of the string. 
# Note: It does not change the original string, but returns a new one.
# Output: I am a coder in hell

print(str.replace("a", "F"))  
# Replaces all occurrences of 'a' with 'F' in the string.
# Output: I Fm A Coder In Hell

print(str.find("a"))  
# Finds the first occurrence of the character 'a' in the string.
# Output: 2

print(str.count("l"))  
# Counts the number of occurrences of the character 'l' in the string.
# Output: 2

# There are more functions available for strings in Python. 
# You can explore them using the dir() function on a string object or referring to Python's documentation.
