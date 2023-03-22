def encoder(oldVar):
    for i in range(len(oldVar)):
        newVar = ""
        if int(oldVar[i]) < 7:
            newVar += str(3 + int(oldVar[i]))
        elif int(oldVar[i]) == 7:
            newVar += "0"
        elif int(oldVar[i]) == 8:
            newVar += "1"
        elif int(oldVar[i]) == 9:
            newVar += "2"
        return newVar


if __name__ == '__main__':
    endvar = True
    while endvar:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            oldVar = input("Please enter your password to encode: ")
            newVar = encoder(oldVar)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {newVar}, and the original password is {oldVar}")
        elif option == 3:
            endvar = False
