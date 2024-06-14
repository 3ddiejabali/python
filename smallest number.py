#A simple program to determine the smallest number among four numbers
a =int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if a<b and a<c and a<d:
    print("the smallest number is",a)
elif b<a and b<c and b<d:
    print("The smallest number is",b)
elif c<a and c<b and c<d:
    print("The smallest number is",c)
else:
    print("The smallest number is",d)

print(min(a,b,c,d),"is the smallest number")