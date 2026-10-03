'''Question 11: Write a Java program to enter marks of five subjects and calculate total marks 
and percentage.

Input:
Marks = 70, 75, 80, 65, 60

Output:
Total = 350
Percentage = 70%

Explanation:
Total marks are calculated by adding all five subject marks.
Percentage = Total / 5.'''
print("Enter marks of five subjects")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=a+b+c+d+e
per=total//5

print("Total =",total)
print("Percentage =",per,"%")
