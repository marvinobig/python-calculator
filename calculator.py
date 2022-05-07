from intro import welcome
from intro import seperator
from operations import add
from operations import minus
from operations import divide
from operations import multiply

welcome()


while True:
    seperator()

    firstNum = int(input("Enter your first number: "))
    secondNum = int(input("Enter your second number: "))

    operation = input("What operation do you want to perform on the number? (add/minus/divide/multiply)  ")

    if operation == "add":
        seperator()
        add(firstNum, secondNum)
        seperator()
    elif operation == "minus":
        seperator()
        minus(firstNum, secondNum)
        seperator()
    elif operation == "divide":
        seperator()
        divide(firstNum, secondNum)
        seperator()
    elif operation == "multiply":
        seperator()
        multiply(firstNum, secondNum)
        seperator()
    else:
        print("No valid operation choosen")

    repeat = input("Do you want to perform another calculation? (y/n)  ")

    if repeat == "y":
        continue
    else:
        break
