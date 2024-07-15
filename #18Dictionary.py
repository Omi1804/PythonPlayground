# Dictionary --> Dictionaries are used to store data values in KEY:VALUE pairs

# They are unordered, mutable (changeable), and do not allow duplicate keys

dick = {
    "name": "Dickhead",
    "class": "Above All",
    "work": "Building Galaxy",
    "age": 100,
    "subjects": ["python", "c++", "java"],
    "isAdult": True
}

print(dick)  # Prints the entire dictionary
print(dick["name"])  # Prints the value associated with the key "name"
print(dick["class"])  # Prints the value associated with the key "class"

dick["age"] = 101  # Updates the value associated with the key "age"
print(dick["age"])  # Prints the updated age

# Appending new key-value pairs
dick["size"] = "20 inch"  # Adds a new key "size" with value "20 inch"
print(dick["size"])  # Prints the value associated with the key "size"

# Nested Dictionaries
students = {
    "name": "Om Nigam",
    "Subjects": {
        "phy": 100,
        "chem": 97,
        "bio": 90
    }
}

print(students["Subjects"]["chem"])  # Prints the value associated with the key "chem" in the nested dictionary
