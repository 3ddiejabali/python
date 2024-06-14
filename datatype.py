#Datatype

number = 78 #int
num = 45.09 #float
greeting = "How are u doing" #str
isProgrammingIntresting = True #bool
devices = ["laptop","computer","tablet","phone"] #list
browser = ("opera","firefox","safari","brave") #tuple
countries = {"Kenya","Uganda","Tanzania"} #set
employee = {
    "firstname" : "Jane",
    "age" : 29,
    "nationality" : "Kenya",
    "email address" : "jane@gmail.com",} #dictionary


print (isProgrammingIntresting)
print (num)
print(countries)
print(employee["firstname"])


#Determining a data type
print(type(countries))
print(type(employee))

#Typecasting is the process of converting one data type to another

print(int(num))
print(float(number))
