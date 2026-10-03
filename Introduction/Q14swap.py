'''Question 14: Write a Java program to swap two numbers using a third variable.
Asked In Basic program
Input:
A = 5
B = 10

Output:
A = 10
B = 5

Explanation:
A temporary variable is used to store one value while swapping the numbers.'''
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=a
a=b
b=c
print("A =",a)
print("B =",b)