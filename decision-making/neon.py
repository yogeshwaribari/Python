'''Question 21: Write a java program to check whether a number is neon or not neon without using 
loop.
Asked In Just Practice assignment
Input:
Number = 9

Output
Neon Number

Explanation:
Square of 9 = 9 * 9 = 81
Sum of digits of 81 = 8 + 1 = 9
Since sum (9) equals the original number (9), it is a Neon Number.'''
n=int(input("Enter number\n"))
sq=n*n
d=sq%10
d1=sq//10
s=d+d1
if s==n:
    print("Neon number")
else:
    print("Not Neon number")
