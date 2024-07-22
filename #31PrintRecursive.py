# WAP to print all elements in a list

def print_recursive(list):
    if(len(list) == 0):
        return 
    
    print(list[0])

    print_recursive(list[1:])


list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print_recursive(list)