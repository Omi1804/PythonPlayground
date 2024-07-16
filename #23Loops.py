# Loops --> are used to repeat instructions
# while loop and for loop

count = 1
while count<=5:
    print("Hello")
    count +=1


# Search for a number x in this tuple using loop
x = int(input("Enter the number to search for : "))

tup = (1,4,9,16,25,36,49,64,81,100)


i = 0
flag = False
while(i<len(tup)):
    if(tup[i] == x):
        print("Your number found in the Tuple")
        flag = True
        break
    i += 1

if(flag == False):
    print("Your number is not in the Tuple")