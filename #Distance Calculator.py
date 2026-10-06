#Distance Calculator
#Converts the distance from kilometers to miles by multiplying the number in kilometers with the value of one kilometer in miles
x=float(input("Enter Distance in kilometers : "))
y=0.621371
#Value of one kilometer in miles
z=x*y
#multiplies the distance and value to convert the kilometers into miles
print("Distance in miles:" ,z)

a=input("Do you want to convert another distance? (yes/no): ")
#asks if you have another distance to be converted into miles
if a=="yes":
    q=float(input("Enter distance in kilometers:"))
    r=q*y
    print("Distance in miles:" ,r)
else:
    print("Program Ended")
