'''Question 3: Write a Java program to check whether a triangle is equilateral, isosceles or scalene.
Asked In Just Practice assignment
Input:
A = 5, B = 5, C = 5

Output:
Equilateral

Explanation:
All sides equal ? Equilateral
Two sides equal ? Isosceles
All sides different ? Scalene'''
a=int(input("Enter side 1\n"))
b=int(input("Enter side 2\n"))
c=int(input("Enter side 3\n"))

if a==b and a==c and b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")