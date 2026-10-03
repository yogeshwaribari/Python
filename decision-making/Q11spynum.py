'''Question 23: Write a java program to Check Number Is Spy Number or Not.
Example : A number is said to be a Spy number if the sum of all the digits is equal to the
 product of all digits.
Asked In Just Practice assignment
Input:
Number = 1412

Output
Spy Number

Explanation:
Sum = 1 + 4 + 1 + 2 = 8
Product = 1 * 4 * 1 * 2 = 8
Since sum = product = 8, it is a Spy Number.'''
num=int(input("Enter number\n"))
s=num//1000+(num%1000)//100+(num%100)//10+num%10
p=(num//1000)*((num%1000)//100)*((num%100)//10)*(num%10)
if s==p:
    print("Spy number")
else:
    print("Not spy number")