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

#  Prompts user to input password, then loops through each digit. Changes the digit to an integer and adds 3. If the new
#  digit is greater than 9, subtracts 10 to account for encoded values that are greater than 10 when increased by 3.
#  Each new digit is then changed to a string and added to the encoded string, which is returned when completed.
def encode():
    original = input("Please enter your password to encode: ")
    encoded = ""
    for digit in original:
        temp_digit = int(digit) + 3
        if temp_digit > 9:
            temp_digit -= 10
        encoded += str(temp_digit)
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
