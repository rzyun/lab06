def encoder(oldVar):
    newVar = ""
    for i in range(len(oldVar)):
        if int(oldVar[i]) < 7:
            newVar += str(3 + int(oldVar[i]))
        elif int(oldVar[i]) == 7:
            newVar += "0"
        elif int(oldVar[i]) == 8:
            newVar += "1"
        elif int(oldVar[i]) == 9:
            newVar += "2"
    return newVar

def decoder(password):#Samir Saldanha
    thing = ''
    for i in password:
        if int(i) > 2:
            thing += str(int(i)-3)
        elif i == '2':
            thing += '9'
        elif i == '1':
            thing+= '8'
        elif i == '0':
            thing += '7'
    return thing

    pass
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
            print(f"The encoded password is {newVar}, and the original password is {decoder(newVar)}")
        elif option == 3:
            endvar = False
