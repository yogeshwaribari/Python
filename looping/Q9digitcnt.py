'''Question 10: Write a java program to count the number of digits in a number
Asked In Just Practice assignment
Input:

Number = 12345

Output:

Number of digits = 5
'''
n=int(input("Enter number\n"))
c=0
while n!=0:
    d=n%10
    
    c+=1
    
    n=n//10
    
print(c)