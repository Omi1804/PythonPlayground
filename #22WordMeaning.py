# Wap to enter marks of 3 subjects form user and store them in dictornary. start with an empty dictionary


marks = {}

x = int(input("Enter Phy : "))
marks.update({"Phy": x})

y = int(input("Enter Maths : "))
marks.update({"Maths": y})

z = int(input("Enter Chem : "))
marks.update({"Chem": z})

print(marks)


# Wap to store 9 and 9.0 as seperate values inside the set 
# store in form of touples
values = {
    ("float",9.0),
    ("int", 9)
}

print(values)