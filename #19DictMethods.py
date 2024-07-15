dick = {
    "name": "Dickhead",
    "class": "Above All",
    "work": "Building Galaxy",
    "age": 100,
    "subjects": ["python", "c++", "java"],
    "isAdult": True
}

# KEYS
print(dick.keys())  # Returns all the keys in the dictionary as a list inside a tuple
# Note: This only includes the outer keys, not the nested keys

# To convert the output into a normal list, use typecasting
listy = list(dick.keys())
print(listy)

# To get the length of the dictionary (number of keys)
print(len(listy))  # First convert keys into a list, then find the length

# VALUES
print(dick.values())  # Returns all the values in the dictionary

# ITEMS
print(list(dick.items()))  # Returns all the items (key-value pairs) in the dictionary

# To get the elements of the dictionary, we have two options
print(dick["age"])  # If there is no value with the given key, it will throw an error
print(dick.get("age2"))  # If there is no value, it will not give an error but just return None

# UPDATE
dick.update({"color": "white"}) # A new key value pair will be added to the dictionary
print(dick)