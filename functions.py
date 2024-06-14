#Inbuilt functions/Standard library functions

y = min(56,336,3,2,25,53)
print(y,"is the minimum number")
z = max(56,336,3,2,25,53)
print(z,"is the maximum number")

x = pow(2,3)
print(x)

#User defined functions
def school():
    print("eMobilis")
school() #This is calling a function

def multiply():
    num1 =5
    num2 =6
    print(num1*num2)
multiply()

#Parameters and Arguments
def add(a,b):
    print(a+b)
add(2,3)
add(21,33)
add(243,3332)
add(266,323)



def employee(Fullname, Age, Salary,Phonenumber,Position):
    print(Fullname,Age,Salary,Phonenumber,Position)
employee("Job Kamau",45,500000000000,25464659629,"MD")
employee("Job Agasa",75,50000000,25467559629,"ENG.")
employee("Riele Dawn",65,50000000,254642059629,"TR")
employee("Capata Gg",54,5000,254726059469,"Sec")