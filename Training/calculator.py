
"""A simple calculator to get used to the syntax of Python"""

def add(x, y):
    """Returns the sum of the two arguments"""
    return x+y

def subtract(x, y):
    """Return the difference of the two arguments"""
    return x-y

#Beginning of the calculator loop

for i in range(0, 5):

    n1 = int(input("Please enter your first number: "))
    n2 = int(input("Second: "))
    operation = input("Please choose whether to add or to subtract: ") 

    if operation == "add":
        print(add(n1, n2))
    elif operation == "subtract":
        print(subtract(n1, n2))
    else:
        print("Please enter a valid operation")
