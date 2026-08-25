#Distance Calculator
#Converts the distance from kilometers to miles
x=float(input("Enter Distance in kilometers : "))
y=0.621371
#Value of one kilometer in miles
z=x*y
#multiplies the distance plus value to convert into miles
print("Distance in miles:" ,z)

a=input("Do you want to convert another distance? (yes/no): ")
#asks if you have another distance to be converted
if a=="yes":
    q=float(input("Enter distance in kilometers:"))
    r=q*y
    print("Distance in miles:" ,r)
else:
    print("Program Ended")