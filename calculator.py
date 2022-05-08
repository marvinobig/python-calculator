import intro
import operations

intro.welcome()


while True:
    intro.seperator()

    try:
        firstNum = int(input("Enter your first number: "))
        secondNum = int(input("Enter your second number: "))
        operation = input("What operation do you want to perform on the number? (add/minus/divide/multiply)  ")
    except ValueError:
        print("Wrong value, bye")
        quit()
        
    if operation == "add":
        intro.seperator()
        operations.add(firstNum, secondNum)
        intro.seperator()
    elif operation == "minus":
        intro.seperator()
        operations.minus(firstNum, secondNum)
        intro.seperator()
    elif operation == "divide":
        intro.seperator()
        operations.divide(firstNum, secondNum)
        intro.seperator()
    elif operation == "multiply":
        intro.seperator()
        operations.multiply(firstNum, secondNum)
        intro.seperator()
    else:
        print("No valid operation choosen")

    repeat = input("Do you want to perform another calculation? (y/n)  ")

    if repeat == "y":
        continue
    else:
        break
