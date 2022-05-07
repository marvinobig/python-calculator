def welcome():
    print("-" * 100)
    print("-" * 100)
    print("""Welcome to The PyCalc
    Use this calculator to perform as many simple maths calculations as you want.""")
    print("-" * 100)
    print("-" * 100)

welcome()

def add(first, second):
    print(f"{first} + {second} is: {first + second}")

def minus(first, second):
    print(f"{first} - {second} is: {first - second}")

def divide(first, second):
    print(f"{first} ÷ {second} is: {first // second}")

def multiply(first, second):
    print(f"{first} x {second} is: {first * second}")


while True:
    print("-" * 20)
    print("-" * 20)
    
    firstNum = int(input("Enter your first number: "))
    secondNum = int(input("Enter your second number: "))

    operation = input("What operation do you want to perform on the number? (add/minus/divide/multiply)  ")

    if operation == "add":
        print("-" * 20)
        print("-" * 20)
        add(firstNum, secondNum)
        print("-" * 20)
        print("-" * 20)
    elif operation == "minus":
        print("-" * 20)
        print("-" * 20)
        minus(firstNum, secondNum)
        print("-" * 20)
        print("-" * 20)
    elif operation == "divide":
        print("-" * 20)
        print("-" * 20)
        divide(firstNum, secondNum)
        print("-" * 20)
        print("-" * 20)
    elif operation == "multiply":
        print("-" * 20)
        print("-" * 20)
        multiply(firstNum, secondNum)
        print("-" * 20)
        print("-" * 20)
    else:
        print("No valid operation choosen")

    repeat = input("Do you want to perform another calculation? (y/n)  ")

    if repeat == "y":
        continue
    else:
        break
