'''Question 9: Write a java program to print a multiplication table of any number.
Asked In Just Practice assignment
Input:

Number = 5

Output:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Explanation:

The program multiplies the given number by values from 1 to 10.
Each result is printed in table format.
'''
n=int(input("Enter number\n"))
i=1
'''
for i in range(i,10+1,1):
    print(n*i)
    
'''
while i<=10:
    print(n*i)
    i+=1
 