'''10.Find Common Even Numbers

Write a Python program to create two sets and display the common elements that are even numbers.
Sample Input:
Set 1 = {2, 3, 4, 5, 12, 35}
Set 2 = {1,2,5,4,6,12}
Sample Output:
2
4
12'''

s1={2,3,4,5,12,35}
s2={1,2,5,4,6,12}
#s3=s1 & s2
s3=set()
for i in s1:
    for j in s2:
        if i==j:
           s3.add(i) 
    
for i in s3:
    if i%2==0:
        print(i)