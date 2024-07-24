# Read the file and replace all instances of the word "Java" with "Python"

# Open the file in read mode ("r") using 'with'
with open("./TextFiles/file1.txt", "r") as f:
    data = f.read()  # Read the entire content of the file

# Replace all occurrences of "Java" with "Python"
new_data = data.replace("Java", "Python")
print(new_data)  # Output the modified content

# Open the file in write mode ("w") using 'with' to overwrite with modified content
with open("./TextFiles/file1.txt", "w") as f:
    f.write(new_data)  # Write the modified content to the file

# From a file containing numbers separated by commas, print the count of even numbers

# Open the file in read mode ("r") using 'with'
with open("./TextFiles/numbers.txt", "r") as f:
    data = f.read()  # Read the entire content of the file

# Split the data into a list of numbers using the split() method
nums = data.split(',')
print(nums)  # Output the list of numbers

# Convert the list of string numbers to integers and count the even numbers
even_count = sum(1 for num in nums if int(num) % 2 == 0)
print(f"Count of even numbers: {even_count}")

# The manual method for splitting and counting (for understanding purpose)

num = ""
num_list = []
for i in data:
    if i == "," or i == "\n":
        if num:
            num_list.append(num)  # Append the number to the list
            num = ""  # Reset the number string
    else:
        num += i  # Build the number string

# Check if there's a leftover number after the loop
if num:
    num_list.append(num)

# Output the manually constructed list of numbers
print(num_list)
