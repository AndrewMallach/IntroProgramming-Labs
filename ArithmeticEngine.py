# CMPT 120 - Lab #6
# Andrew Mallach
# 10-25-2018
###


def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', 'power', and 'quit'.\n")


def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def inputNumber():
    global num1, num2
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

def doLoop():
    while True:

        global result
        

        cmd = input("What computation do you want to perform? ")
        editCmd = cmd.strip().lower()
       


        if editCmd == "add":
             inputNumber()
             result = num1 + num2
        elif editCmd == "sub":
             inputNumber()
             result = num1 - num2
        elif editCmd == "mult":
             inputNumber()
             result = num1 * num2
        elif editCmd == "div":
             inputNumber()
             result = num1 // num2
        elif editCmd == "quit":
             break
        elif editCmd == "power":
            inputNumber()
            result = num1**num2
        else:
            print("\n", editCmd, " is not a valid command.\n")
            continue
            

        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()


main()


