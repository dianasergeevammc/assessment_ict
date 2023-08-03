# function goes here (top of code)

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

# main routine starts here


num_1=int_check("choose 'low' <1-10>: ", 1, 10)
num_2=int_check("choose 'high' <10-20>: ", 10, 20)

print()
print("Low: {}".format(num_1))
print("high: {}".format(num_2))
