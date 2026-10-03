'''Question 5: Write a Java program to enter the radius of a circle and calculate its diameter,
 area, and circumference.
Asked In Basic program
Input:
Radius = 7

Output:
Diameter = 14
Area = 153.86
Circumference = 43.96

Explanation:
Diameter = 2 * radius
Area = ? * r^2
Circumference = 2 * ? * r
The formulas are applied using the given radius.'''
r=input("Enter Radius\n")
dia=2*int(r)
area=3.14*(int(r)**2)
circumference=2*3.14*int(r)

print("Diameter =",dia)
print("Area =",area)
print("Circumference =",circumference)
