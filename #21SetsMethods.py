# Sets Methods

# Initialize a set with some elements. Note that sets automatically eliminate duplicate values.
collection = {1, 2, 3, 4, "hello"}

# Add the elements to the set. 'add' method adds a single element to the set.
collection.add("world")
collection.add((8,9,10,11))  # Adding a tuple to the set.

# Remove an element from the set. If the element is not found, 'remove' will raise a KeyError.
collection.remove("hello")

# Emptied the whole set
# collection.clear() # This clears the entire set, leaving it empty.

# 'pop' removes and returns a random element from the set.
print(collection.pop())  # Note that the element removed is random.

# Union --> Combines both set values and returns a new set containing all unique elements.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))  # All unique values from both sets will be combined.

# Intersection --> Returns a new set containing only the common values from both sets.
print(set1.intersection(set2))  # Only the common values will be returned.
