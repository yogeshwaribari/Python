'''Question 2: Write a java program to print all natural numbers in reverse (from n to 1). 
using a while loop.
Asked In Just Practice assignment
Input:

n = 5

Output:

5 4 3 2 1
'''
n=int(input("Enter number\n"))
'''
i=n
while i>=1 :
    print(i,end=" ")
    i-=1
    '''
for i in range(n,0,-1):
    print(i,end=" ")