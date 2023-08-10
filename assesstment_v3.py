# code for the calculator taken and modified from https://www.programiz.com/python-programming/examples/calculator
# This function does the calculation for a perimeter of a rectangle/square next on the list is the shape selector
# this library imports number pi to calculate the circle
import math

# checks if the user has entered yes or no


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("!!! - Please answer yes(Y) or no(N).")


# checks if response isn't blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Try again.. ")

        else:
            return response


# checks the dimentions of the shape to be not lower than 0 or higher than a 100
def int_check(question, low, high):
    error = "!!! Error - Please enter an integer between {} and {}".format(low, high)
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

# main routine starts here

# asks if the user wants instructions


while True:

    want_instructions = yes_no("✩- Do you want to read the instructions? ")

    if want_instructions == "yes":
        print()
        print("✩✩✩")
        print()
        print(" ✩- This calculator does area equations for you.\n " 
              "✩- You will be given five (5) shapes to choose from, \n "
              "and once you do at least one (1) calculation, "
              "you can press ENTER to quit the application.\n "
              "✩- Once you quit, you can choose whether or not you want your calculation history. \n "
              "✩- All of the equations are done in centimetres (cm). \n "
              "✩- No decimals (numbers like 12.34), letters (like x), and blanks are allowed.")

    print()
    print("✩✩✩")
    print()
    print("✩- Shape list:")
    print("1. Square:")
    print("2. Rectangle:")
    print("3. Triangle:")
    print("4. Circle:")
    print("5. Parallelogram:")

    # variable that allows the loop to run
    next_calculation = ""

    # a loop which will keep on going and calculating until the user presses enter
    while next_calculation == "":

        # take input from the user
        choice = int_check("✩- Enter the number of the shape you want to calculate: ", 1, 5)

        # check if choice is one of the five options

        if choice == 1:
            side = int_check("✩- Enter the side (1=min, 100=max): ", 1, 100)
            print(">>>", side, "^", "2", "=", square(side))

        elif choice == 2:
            side = int_check("✩- Enter the side (1=min, 100=max): ", 1, 100)
            length = int_check("✩- Enter the length (1=min, 100=max): ", 1, 100)
            print(">>>", side, "*", length, "=", rectangle(side, length))

        elif choice == 3:
            base = int_check("✩- Enter the base (1=min, 100=max): ", 1, 100)
            length = int_check("✩- Enter the side (1=min, 100=max): ", 1, 100)
            print(">>>", "1/2", "*", base, "*", length, "=", triangle(base, length))

        elif choice == 4:
            radius = int_check("✩- Enter the radius (1=min, 100=max): ", 1, 100)
            print(">>>", "π", "*", radius, "^", "2", "=", circle(radius))

        else:
            side = int_check("✩- Enter the side (1=min, 100=max): ", 1, 100)
            length = int_check("✩- Enter the length (1=min, 100=max): ", 1, 100)
            print(">>>", side, "*", length, "=", parallelogram(side, length))

        # check if user wants another calculation
        # break the while loop if answer is xxx
    next_calculation = input("✩- Press enter to continue or press anything to exit the calculator: ")

    print()
    print("✩✩✩")
    print()