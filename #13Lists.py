# Array-like data structure in Python is called a List
# Lists can store elements of different types (integer, float, string, etc.)

marks = [14, 32.3, 33, 34, 35, 36, 37, 38, 39]

print(marks)  # Prints the entire list

print(len(marks))  # Prints the length of the list

print(marks[2])  # Prints the element at index 2 of the list (33 in this case)

# In Python, lists are different from arrays as they can contain elements of various types

student = ["karan", 43.3, 34, "delhi"]

# Strings are immutable in Python, meaning their content cannot be changed
# Lists are mutable, meaning their content can be changed

student[0] = "Om"  # Modifies the first element of the list
print(student)  # Prints the updated list
