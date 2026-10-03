'''Question 11: Write a java program to calculate the sum of digits in a number.
Asked In Just Practice assignment
Input:

Number = 1234

Output:

Sum of digits = 10

Explanation:

The program separates each digit using modulus (%) and division (/).
Digits are 1, 2, 3, 4 and their sum is 1 + 2 + 3 + 4 = 10.'''

n=int(input("Enter number\n"))
sum=0
while n!=0:
    d=n%10
    sum+=d
    n=n//10
print("sum =",sum)
