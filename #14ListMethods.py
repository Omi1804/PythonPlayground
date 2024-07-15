# List specific methods in Python

marks = [114, 32.3, 33, 34, 35, 36, 37, 38, 39]

# Slicing in lists
print(marks[1:4])  # Outputs elements from index 1 to 3 (does not include index 4)
# Lists also support negative indexes for slicing

# Append elements
marks.append(1000)  # Adds one element (1000) at the end of the list

# Sort the list
marks.sort()  # Sorts the list in ascending order
print(marks)

fruits = ["bnana", "apple", "lichi"]  # A list of fruits

# Sort the list of fruits in alphabetical order
fruits.sort()
print(fruits)

# Sort the list in descending order
marks.sort(reverse=True)  # Sorts the list in descending order
print(marks)

# Reverse the list
marks.reverse()  # Reverses the order of the list
print(marks)

# Insert an element at a particular index
marks.insert(2, 10)  # Inserts the element 10 at index 2
print(marks)

# Remove the first occurrence of an element
marks.remove(35)  # Removes the first occurrence of the element 35
print(marks)

# Remove the element at a specific index
marks.pop(5)  # Removes the element at index 5
print(marks)
