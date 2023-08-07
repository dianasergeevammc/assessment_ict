# code for the calculator taken and modified from https://www.programiz.com/python-programming/examples/calculator
# This function does the calculation for a perimeter of a rectangle/square next on the list is the shape selector
import math

# checks the dimentions of the shape to be not lower than 0 or higher than a 100
def int_check(question, low, high):
    error = "please enter an integer between {} and {}".format(low, high)
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return(response)
            else:
                print(error)
        except ValueError:
            print(error)

# this function calculates the area of a square
def square(x):
    return x ** 2


# This function calculates the area of a rectangle
def rectangle(x, y):
    return x * y


# This function calculates the area of a triangle
def triangle(x, y):
    return 1/2 * x * y


# This function calculates the area of a circle
def circle(x):
    return math.pi * x ** 2


# this function calculates the area of a parallelogram
def parallelogram(x, y):
    return x * y


print("Select operation:")
print("1. Area of a square:")
print("2. Area of a rectangle:")
print("3. Area of a triangle:")
print("4.Area of a circle:")
print("5.Area of a parallelogram:")

next_calculation = ""

while next_calculation == "":
    # take input from the user
    choice = int_check("Enter choice(1/2/3/4/5): ", 1, 5)

    # check if choice is one of the five options
    #if choice in ('1', '2', '3', '4', '5'):

    if choice == 1:
        side = int_check("Enter the side (1=min, 100=max): ", 1, 100)
        print(side, "^", "2", "=", square(side))

    elif choice == 2:
        side = int_check("Enter the side (1=min, 100=max): ", 1, 100)
        length = int_check("Enter the length (1=min, 100=max): ", 1, 100)
        print(side, "*", length, "=", rectangle(side, length))

    elif choice == 3:
        base = int_check("Enter the base (1=min, 100=max): ", 1, 100)
        length = int_check("Enter the side (1=min, 100=max): ", 1, 100)
        print("1/2", "*", base, "*", length, "=", triangle(base, length))

    elif choice == 4:
        radius = int_check("Enter the radius (1=min, 100=max): ", 1, 100)
        print("π", "*", radius, "^", "2", "=", circle(radius))

    else:
        side = int_check("Enter the side (1=min, 100=max): ", 1, 100)
        length = int_check("Enter the length (1=min, 100=max): ", 1, 100)
        print(side, "*", length, "=", parallelogram(side, length))

    # check if user wants another calculation
    # break the while loop if answer is xxx
    next_calculation = input("press enter to continue OR type anything to quit: ")


print("The program has ended")