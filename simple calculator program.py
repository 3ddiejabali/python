num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operation = input("Enter operation:"
                  "+ for addition"
                  "- for subtraction"
                  "* for multiplication"
                  "/ for division")
if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid input")