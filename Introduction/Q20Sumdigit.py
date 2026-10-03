'''Question 20: Write a Java program to compute the sum of digits of an integer.
Asked In Basic program
Input:
123

Output:
6

Explanation:
Each digit is separated using modulus and division operations.
1 + 2 + 3 = 6.
'''
n=int(input("Enter Number\n"))
d=n//100
dsum=d
rem=n%100
d=rem//10
rem=rem%10
dsum+=d+rem
print("Sum =",dsum)