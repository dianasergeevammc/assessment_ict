# code for the calculator taken and modified from https://www.programiz.com/python-programming/examples/calculator
# This function does the calculation for a perimeter of a rectangle/square
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

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5 or press 'xxx' to quit): ")

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num_1 = int_check("choose 1st value (1=min, 100=max): ", 1, 100)
            num_2 = int_check("choose 2nd value (1=min, 100=max): ", 1, 100)
        except ValueError:
            print("Invalid input. Please enter a number for a valid shape choice.")
            continue

        if choice == '1':
            print(num_1, "^", "2", "=", square(num_1))

        elif choice == '2':
            print(num_1, "*", num_2, "=", rectangle(num_1, num_2))

        elif choice == '3':
            print("1/2", "*", num_1, "*", num_2, "=", triangle(num_1, num_2))

        elif choice == '4':
            print("π", "*", num_1, "^", "2", "=", circle(num_1))

        elif choice == '5':
            print(num_1, "*", num_2, "=", parallelogram(num_1, num_2))

        # check if user wants another calculation
        # break the while loop if answer is xxx
        next_calculation = input("press anything to continue OR type 'xxx' to quit ")
        if next_calculation == "xxx":
            break
    else:
        print("invalid input.")