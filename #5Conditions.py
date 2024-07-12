# if-elif-else in Python

# Python is an indentation-sensitive language
# Proper indentation is crucial in Python

light = input("light: ")  # Get user input for the traffic light color
if light == "red":
    print("Stop")  # If the light is red, print "Stop"
elif light == "green":
    print("Go")  # If the light is green, print "Go"
else:
    print("Wait")  # If the light is neither red nor green, print "Wait"

# Example 2: Grading system based on marks
marks = int(input("Marks: "))  # Get user input for marks
if marks >= 90:
    print("A")  # If marks are 90 or above, print grade "A"
elif 80 <= marks < 90:
    print("B")  # If marks are between 80 and 89, print grade "B"
elif 70 <= marks < 80:
    print("C")  # If marks are between 70 and 79, print grade "C"
else:
    print("D")  # If marks are below 70, print grade "D"

# Ternary Operators in Python

food = input("food: ")  # Get user input for food
eat = "Yes" if food == "cake" else "No"  # Ternary operator to determine if food is "cake"

print(eat)  # Print "Yes" if food is "cake", otherwise print "No"

# In Python, the ternary operator syntax is different from JS or C++
# <statement1> if <condition> else <statement2>

print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")
# Another example: print "sweet" if food is "cake" or "jalebi", otherwise print "not sweet"

# Another way of writing ternary statements
# Clever Ternary Operator

age = int(input("Age: "))  # Get user input for age
vote = ("yes", "no")[age < 18]
# In this format, the condition in the square brackets is checked.
# If the condition holds true (age < 18), the second element ("no") is chosen.
# If the condition is false, the first element ("yes") is chosen.

sal = float(input("salary: "))  # Get user input for salary
tax = sal * (0.1, 0.2)[sal > 50000]
# Similarly, in this ternary format, the condition in the square brackets is checked.
# If the condition holds true (sal > 50000), the second element (0.2) is chosen.
# If the condition is false, the first element (0.1) is chosen.
