# Ask user for calculation or exit the program
while True:
    userInput = input("Would you like to add/sub(subtract)/mul(multiply)/div(divide)? or Type 'exit' to stop now!").lower( )
    # Checking user input
    if userInput == "exit":
        print("Thank you for your checking!")
        break
    else:
        if userInput == "sub":
            print("You wrote {}, it means you chose 'subtract'.".format(userInput))
        elif userInput =="div":
            print("You wrote {}, it means you chose 'divide'.".format(userInput))
        elif userInput =="mul":
            print("You wrote {}, it means you chose 'multiply'.".format(userInput))
        elif userInput == "add":
            print("You chose {}.".format(userInput))
        else:
            print("Wrong Input")
            break
        try:
            num1 = float(input("What is the first number? "))
            num2 = float(input("What is the second number? "))
            if userInput == "add":
                result = num1 + num2
                print( "{} + {} = {}".format(num1, num2, result))
            elif userInput == "sub":
                result = num1 - num2
                print( "{} - {} = {}".format(num1, num2, result))
            elif userInput == "mul":
                result = num1 * num2
                print( "{} * {} = {}".format(num1, num2, result))
            elif userInput == "div":
                result = num1 / num2
                print( "{} / {} = {}".format(num1, num2, result))
            else:
                print("Sorry, but '{}' is not an option.".format(userInput))
        except:
            print("Error: Input problem, please try again!")
            break
