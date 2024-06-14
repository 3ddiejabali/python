firstname = input("Enter Firstname:")
print("My Firstname is",firstname)

lastname = input("Enter Lastname:")
print("My Lastname is",lastname)

age =int(input("Enter Age:"))
print("I am",age,"years old")

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
operand = input("Enter operator:"
                "+ for addition"
                "- for subtraction"
                "* for multiplication"
                "/ for division")
if operand == "+":
    print(num1+num2)
elif operand == "-":
    print(num1-num2)
elif operand == "*":
    print(num1*num2)
elif operand == "/":
       if num2 == 0:
           print("Error!Division by zero")
       else:
           print(num1/num2)
else :
 print("Invalid input")