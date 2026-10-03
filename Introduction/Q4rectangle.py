'''Question 4: Write a Java program to enter length and breadth of a rectangle and calculate 
its area.
Asked In Basic program
Input:
Length = 10
Breadth = 5

Output:
Area = 50

Explanation:
The area of a rectangle is calculated using the formula:
Area = Length * Breadth
So, 10 * 5 = 50.'''
len=input("Enter length\n")
breadth=input("Enter breadth\n")

area=int(len)*int(breadth)
print("Area =",area)