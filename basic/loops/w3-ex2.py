print("Please enter a choice\n\n1-See a nice message\n2-Calculate area of a rectangel\n3-Area of trapezium\n4-Times table")
opt = int(input())
  
if opt== 1:
  print("You do not smell to bad today!")
elif opt == 2:  
  lenght =float(input("Enter lenght: "))
  width = float(input("Enter width: "))
  area =lenght*width
  print(f"Area of rectangle is  {area} cm^2")
elif opt == 3:  
  base1 =float(input("Enter 1st base: "))
  base2 = float(input("Enter 2nd base: "))
  height= float(input("Enter height: "))
  area=(base1+base2)*height/2
  print(f"The area of trapezium is: {area}")
elif opt ==4:
  n=int(input("Enter a number"))
  for i in range(1,11):
    print(f"{i}x{n}= {i*n}")
  print("That's all folks!")
else:
  print("No such option , go to Lidl")
  