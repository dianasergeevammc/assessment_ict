# define a blank dictionary with no element
import pandas
# lists to hold ticket details
# dictionary to hold ticket details


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


# shape list for testing
def square(x):
    return x ** 2


max_calculations = 2
start_calculations = 0
filename = "test"

all_names = []
shapes_answers = []

while start_calculations < max_calculations:
    side = int_check(">Enter the side (1=min, 100=max): ", 1, 100)
    print(side, "^", "2", "=", square(side))
    convert_ans = int(square(side))
    shapes_answers['shape_answers'].append(convert_ans)
    start_calculations += 1

calc_dict = {
    "Shape": all_names,
    "Shape Area": shapes_answers
}
calc_frame = pandas.DataFrame(calc_dict)


calc_string = pandas.DataFrame.to_string(calc_frame)

to_write = [calc_string]

for item in to_write:
    print(item)

# write output to file
# create file to hold data
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()


