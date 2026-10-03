'''Question 5: Write a java program to print all odd numbers between 1 to 100.
Asked In Just Practice assignment
Input:

No input required

Output:

1 3 5 7 ... 99
'''
i=1
while i<=100:
    if i%2!=0 :
        print(i,end=" ")
    i+=1