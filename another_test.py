def add_user_input_to_dictionary():
    # Create an empty dictionary to store user inputs
    user_info = {}

    for i in range(6):
        key = input(f"Enter key {i + 1}: ")
        value = input(f"Enter value {i + 1}: ")
        user_info[key] = value

    return user_info


# Example usage:
user_data = add_user_input_to_dictionary()
print("User data:", user_data)

