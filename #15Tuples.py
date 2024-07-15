# Tuples
# A built-in data type that lets us create immutable sequences of values

tup = (1, 2, 3, 4, 5)
print(tup[0])  # Prints the first element of the tuple

# tup[0] = 5  # This is not allowed in tuples as they are immutable

# Empty tuple
tup2 = ()

# Single value tuple
tup3 = (1,)  # Comma is important for a single value; otherwise, it will be considered an integer

# Slicing in tuples
print(tup[1:3])  # Outputs elements from index 1 to 2 (does not include index 3)

# Methods in tuples
print(tup.index(3))  # Returns the index of the first occurrence of the element 3

print(tup.count(2))  # Counts the total occurrences of the value 2
