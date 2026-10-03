'''Question 10: Write a Java program to calculate the area of an equilateral triangle.
Asked In Basic program
Input : Side = 6
Output : Area = 15.59
Explanation : Area is calculated using the formula for equilateral triangles.'''
import math
s=input("Enter Side\n")
e=(math.sqrt(3)/4)*(int(s)**2)
print("Area =",e)
