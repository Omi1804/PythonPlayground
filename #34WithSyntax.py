# The use of the 'with' keyword is to open files with aliases and automatically handle closing the file.

# Open the file in read mode ("r") using 'with'
with open("./TextFiles/file1.txt", "r") as f:
    data = f.read()  # Read the entire content of the file
    print(data)  # Output the content

# Open the file in write mode ("w") using 'with'
with open("./TextFiles/file2.txt", "w") as f:
    f.write("new Data")  # Write "new Data" to the file

# When using 'with', you don't need to explicitly close the file. 
# 'with' handles it automatically, making the code cleaner and reducing the risk of file-related errors.


# Deleting the file
# Delete is not natively supported by python but we have to use modules to use it

# using os module here

import os
os.remove("./TextFiles/file2.txt") # now file2.txt is removed