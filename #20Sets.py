# A set is a collection of unordered items
# Each element in the set must be unique and immutable

# In a set, we can store boolean, int, float, string, and tuples as they are immutable,
# but we cannot store list and dictionary as they are mutable

# Remember that set itself is mutable that we can add or remove the values in set but its elements are immutable

collection = {1, 2, 3, 4, 4, "hello", "hello"}  # This is how we create a set
# Notice that duplicate values are removed
print(collection)  # Output: {1, 2, 3, 4, 'hello'}
print(type(collection))  # Output: <class 'set'>

# Length of the set
print(len(collection))  # Output: length of all unique items in the set, which is 5

# Creating an empty set
# If I write
empSet = {}  # This creates an empty dictionary, not a set

# Hence, to create an empty set, we write
realEmptySet = set()  # This is the correct way to create an empty set
print(realEmptySet)  # Output: set()
print(type(realEmptySet))  # Output: <class 'set'>
