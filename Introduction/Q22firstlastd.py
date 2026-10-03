'''Question 22: Write a Java program to find the first and last digit of a three-digit number 
without using a loop.
Asked In Basic program
Input:
456

Output:
First = 4
Last = 6

Explanation:
The first digit is obtained by dividing the number by 100.
The last digit is obtained using the modulus operator (% 10).'''
n=int(input("Enter number :"))
f=n//100
l=n%10
print("First =",f)
print("Last =",l)
