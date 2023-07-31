# code for the calculator taken and modified from https://www.programiz.com/python-programming/examples/calculator
# This function does the calculation for a perimeter of a rectangle/square
import math


def square(x):
    return x ** 2


# This function calculates the area of a rectangle/square
def rectangle(x, y):
    return x * y


# This function multiplies two numbers
def triangle(x, y):
    return 1/2 * x * y


# This function divides two numbers
def circle(x):
    return math.pi * x ** 2


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

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number for a valid shape choice.")
            continue

        if choice == '1':
            print(num1, "^", "2", "=", square(num1))

        elif choice == '2':
            print(num1, "*", num2, "=", rectangle(num1, num2))

        elif choice == '3':
            print("1/2", "*", num1, "*", num2, "=", triangle(num1, num2))

        elif choice == '4':
            print("π", "*", num1, "^", "2", "=", circle(num1))

        elif choice == '5':
            print(num1, "*", num2, "=", parallelogram(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("press anything to continue OR type 'xxx' to quit ")
        if next_calculation == "xxx":
            break
    else:
        print("invalid input.")