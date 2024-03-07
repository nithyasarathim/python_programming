print("To find area of rectangle :")
length=int(input("Enter the length :"))
breadth=int(input("Enter the breadth :"))
print("The area of the rectangle is :",length*breadth)

print("\nTo find area of the cube")
a=int(input("Enter the length of the cube:"))
print("The area of the cube is :",a*a*a)

print("\nEnter three numbers to find the largest among them :")
a=int(input("Enter the number 1 :"))
b=int(input("Enter the number 2 :"))
c=int(input("Enter the number 3 :"))
if(a>b and a>c):
  print(a," is largest")
elif(b>a and b>c):
  print(b," is largest")
elif(c>a and c>b):
   print(c," is largest")

age=int(input("\nEnter the age category to find (1-99):"))
if(age>=1 and age<=12):
  print("\nKID")
elif(age>12 and age<=19):
  print("\nTEEN")
elif(age>19 and age<=30):
  print("\nADULT")
elif(age>30 and age<=40):
  print("\nMATURED ADULT")
elif(age>40 and age<80):
  print("\nSENIOR CITIZEN")
else:
  print("\nDECEASED")

num=int(input("Enter the number for factorial :"))
fact=1;
for i in range(1,num+1,1):
  fact=fact*i
print("The factorial of ",num,"is :",fact)

