# code for the calculator taken and modified from https://www.programiz.com/python-programming/examples/calculator
# This function does the calculation for a perimeter of a rectangle/square next on the list is the shape selector
# this library imports number pi to calculate the circle
import math

# yes / no function for instructions for a calculator


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"
        else:
            print("!!! - Please answer yes(Y) or no(N).")


# checks the dimensions of the shape to be not lower than 0 or higher than a 100
def int_check(question, low, high):
    error = "please enter an integer between {} and {}".format(low, high)
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
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


# the user starts out with 6 calculations available so
# that the program doesn't get overwhelmed with too many user inputs.
max_calculations = 6
start_calculations = 0


# state the filename to then put into the final file
filename = "Calculation History"

calculation_history = []

# main routine starts here

# asks if the user wants instructions


want_instructions = yes_no("do you want to hear the instructions? ")

if want_instructions == "yes":
    print()
    print("---")
    print()
    print(" > This calculator does area equations for you.\n "
          "> You will be given five (5) shapes to choose from, \n "
          "and once you do at least one (1) calculation, "
          "you can press ENTER to quit the application.\n "
          "> Once you quit, you can choose whether or not you want your calculation history. \n "
          "> All of the equations are done in centimetres (cm). \n "
          "> No decimals (numbers like 12.34), letters (like x), and blanks are allowed.")


print()
print("---")
print()
print("Select operation:")
print("1. Area of a square:")
print("2. Area of a rectangle:")
print("3. Area of a triangle:")
print("4.Area of a circle:")
print("5.Area of a parallelogram:")

# variable that allows the loop to run
next_calculation = ""

# a loop which will keep on going and calculating until the user presses enter
while next_calculation == "" and start_calculations < max_calculations:
    # take input from the user
    choice = int_check(">Enter the number of the shape you want to calculate: ", 1, 5)

    # check if choice is one of the five options
    # if choice in ('1', '2', '3', '4', '5'):

    if choice == 1:
        side = int_check("> Enter the side (1=min, 100=max): ", 1, 100)
        start_calculations += 1
        print(side, "^", "2", "=", square(side))
        result = square(side)

    elif choice == 2:
        side = int_check("> Enter the side (1=min, 100=max): ", 1, 100)
        length = int_check("> Enter the length (1=min, 100=max): ", 1, 100)
        start_calculations += 1
        print(side, "*", length, "=", rectangle(side, length))
        result = rectangle(side, length)

    elif choice == 3:
        base = int_check("> Enter the base (1=min, 100=max): ", 1, 100)
        length = int_check("> Enter the side (1=min, 100=max): ", 1, 100)
        start_calculations += 1
        print("1/2", "*", base, "*", length, "=", triangle(base, length))
        result = triangle(base, length)

    elif choice == 4:
        radius = int_check("> Enter the radius (1=min, 100=max): ", 1, 100)
        start_calculations += 1
        print("π", "*", radius, "^", "2", "=", circle(radius))
        result = circle(radius)

    else:
        side = int_check("> Enter the side (1=min, 100=max): ", 1, 100)
        length = int_check("> Enter the length (1=min, 100=max): ", 1, 100)
        start_calculations += 1
        print(side, "*", length, "=", parallelogram(side, length))
        result = parallelogram(side, length)
# appends the number inputs into the dictionary
    calculation = {"Shape": choice, "Result": result}
    calculation_history.append(calculation)

    # check if user wants another calculation
    # break the while loop if answer is anything other than ENTER
    if start_calculations == max_calculations:
        print("you have done all calculations available.")
        break
    else:
        print("you have done {} calculations. there is"
              " {} calculations available".format(start_calculations, max_calculations - start_calculations))

    next_calculation = input("Press ENTER to continue or type a letter to quit: ")

to_write = [calculation_history]

write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(str(item))


# close file
text_file.close()
