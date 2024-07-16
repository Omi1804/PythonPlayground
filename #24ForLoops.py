# For loop --> used for sequential traversal. For traversing lists, strings, tuples, etc.

# Example with a list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list:
    print(num)

# Example with a tuple
tup = (1, 2, 3, 4)
for i in tup:
    print(i)

# Example with a string
str = "Hello mere bcce kyaa tum sex krna cahte ho"
# Uncomment the lines below to print each character in the string
# for i in str:
#     print(i)

# For loop can also have an else clause, which runs at the end of the loop if the loop is not terminated by a break statement
for i in str:
    print(i)
else:
    print("END")

# We can use the else clause in situations where we need to check if an element was found in the iterable
for i in str:
    if i == "z":
        print("found z")
        break
else:  # This else is associated with the for loop, not the if condition
    print("Did not find z")
