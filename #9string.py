# Escape sequence characters
# \n makes string start form next line 

str1 = "This is the string. \n we are creating next line in python"
print(str1)

# Operations in strings in Python

# Concatenation
a = "apna"
b = "college"
print(a + " " +b)

# length of the string 
print(len(a))

# to get the character in the string
ch = str1[2]
print(ch)


# Slicing --> Accessing part of the string
strNew = "Apna_college"
print(strNew[1:4]) 
# [1:4] --> first character is excluded and last character is included

print(strNew[3:]) # Here it assumes after 3rd index to last index

print(strNew[-5:-1]) # last character is is -1 and then so on