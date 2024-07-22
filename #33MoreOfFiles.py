# Reading a File

# Open the file in read mode ("r")
f = open("./TextFiles/file1.txt", "r") 

# Read the first 3 characters from the file
data = f.read(3)
print(data)  # Output the first 3 characters

# Read one line at a time from the file
line1 = f.readline()
print(line1)  # Output the first line after the first 3 characters

line2 = f.readline()
print(line2)  # Output the second line

# Close the file to free up resources
f.close()

# Remember: if a part of the file has already been read by another function,
# the read pointer moves past that part, so readline will read from the new pointer position.
# That's why line1 starts from "lo" instead of "Hello" as "Hel" has already been read by data.

# Writing to a File
# We can write to the file in two ways:
# 1. Using "w" -> overwrites the file
# 2. Using "a" -> appends to the end of the file

# Open the file in write mode ("w") - this will overwrite the file
f = open("./TextFiles/file1.txt", "w")
f.write("I am the king of the Development")  # Overwrite the file with this text
f.close()

# Open the file in append mode ("a") - this will append to the file
f = open("./TextFiles/file1.txt", "a")
f.write("\nNow I am starting to understand")  # Append this text to the file
f.close()


# If we open a file in "w" or "a" mode and the file doesn't exist then python will create the file for us


# there are more modes like "w+" , "r+" etc which has different functions