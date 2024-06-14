#Arithmetic operators -used to perform simple calculations

num1 = 56
num2 = 8

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)#modulus returns the remainder after division of numbers

#Comparison operator-used to compare values
print(num1 < num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)#Equal to
print(num1 != num2)#Not equal

#Assignment operators-used to assign values to variables
a = 200
print(a)

a /= 20
print(a)

#Logic operators - and , or , not
x =100
print(x<250 and x>1000)
print(x<250 or x>1000)
print(not(x<250 or x>1000))
print(not(x<250 and x>1000))

#opereator precedence - this is the order in which operations get executed

output = (100-4*3/1)
print(output)
print(int(output))

#Write a simple python program that returns the area of a trapezium

#A=1/2(a+b)H
base1 = 10
base2 = 10
height = 5
area = 1/2*(base1+base2)*height
print (area)

#Conditional statements
temperature = 46

if temperature < 25:
    print("It is cold")
elif temperature >25:
      print("It is hot")
else:
     print("Normal temperature")



#Simple programme to return the largest number among three numbers
first = 90
second = 45
third = 60

if first > second and first> third:
    print(first,"the largest number")
elif second> first and second> third:
    print(second,"the largest number")
else:
    print(third,"the largest number")

#write a python programme that checks whether a number is even or odd
num=0
if num == 0:
    print(num, "neutral")
elif num % 2 == 0:
    print(num,"even")
else:
    print(num,"odd")





