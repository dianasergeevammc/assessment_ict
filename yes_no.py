# main routine goes in here
def yes_no(question):
    response = input(question).lower()

    if response == "yes" or response == "y":
        return "yes"

    elif response == "no" or response == "n":
        pass
    else:
        print("oh MY GOD. CHOOSE YES/NO.")


want_instructions = yes_no("do you want to hear the"
                          " instructions??? ")
if want_instructions == "yes":
    print("instructions are here")

print("all done, now")
print()