# File I/O in Python
# Python can be used to perform operations like reading and writing data on files.

# Types of files:
'''
Text Files: .txt, .docx, .log etc.
Binary Files: .mp4, .mov, .png, .jpeg etc.
'''

# We have to open a file before reading or writing

# Syntax to open a file:
# f = open("file_name", "mode")
# mode can be 'r' or 'w' i.e., read or write

# Example: Reading from a text file
f = open("./TextFiles/file1.txt", "r")  # Open file in read mode
data = f.read()  # Read the contents of the file
print(data)  # Print the file contents
f.close()  # Close the file

# Different Modes of Files:
'''
'r'  = open for reading (default)
'w'  = open for writing, truncating the file first
'x'  = create a new file and open it for writing
'a'  = open for writing, appending to the end of the file if it exists
'b'  = binary mode
't'  = text mode (default)
'+'  = open a disk file for updating (reading and writing)
'''
