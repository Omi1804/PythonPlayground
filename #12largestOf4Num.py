# Calculate the largest of four numbers

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

# Using a series of if-elif-else statements to determine the largest number
if a > b and a > c and a > d:
    print("The largest of the four numbers is", a)
elif b > a and b > c and b > d:
    print("The largest of the four numbers is", b)
elif c > a and c > b and c > d:
    print("The largest of the four numbers is", c)
else:
    print("The largest of the four numbers is", d)
