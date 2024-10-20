# Melissa Cote

# Prints the menu and prompts user for menu selection.
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    choice = int(input("Please enter an option: "))
    return choice

# Takes in a password in string format containing only integers. Encodes by converting each digit in the password to an
# integer, adding 3, then converting the digit back to a string. Each digit is added to the variable "encoded", which
# stores the final encoded password.
def encode():
    original = input("Please enter your password to encode: ")
    encoded = ""
    for digit in original:
        encoded += str(int(digit) + 3)
    print("Your password has been encoded and stored!")
    return encoded

def decode(encoded):
    pass

# On program start, prints the menu and gets the first menu selection. For option 1, calls the encode function, then
# displays the menu. For option 2, calls the decode function, then displays the menu. If the user selects option 3,
# the program is terminated.
def main():
    menu_selection = menu()
    while True:
        if menu_selection == 1:
            encoded_password = encode()
            print()
            menu_selection = menu()

        elif menu_selection == 2:
            decode(encoded_password)
            print()
            menu_selection = menu()

        elif menu_selection == 3:
            break




if __name__ == '__main__':
    main()
