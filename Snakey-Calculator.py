
#Build a Calculator
def calculator ():
    while True:
        while True:
            print("Pick an option: 1 for Additions, 2 for Subtraction, 3 for Multiplication, 4 for Division, 5 for Modulo, or Q to quit")
            selection = input("Enter your choice: ")
            if selection == "q" or selection == "Q":
                print ("Quitting...")
                print("Thank you for using Snakey Calculator! Goodbye!")
                break

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            if selection == "1": result = num1 + num2
            elif selection == "2": result = num1 - num2
            elif selection == "3": result = num1 * num2
            elif selection == "4": result = num1 / num2
            elif selection == "5": result = num1 % num2
            else:
                print("Invalid option, try again")
                continue
            print (result)
        restart = input("Do you want to restart? (y/n): ")
        if restart == "n" or restart == "N":
            print ("See you next time!")
            break

calculator()

print ("------------------")



