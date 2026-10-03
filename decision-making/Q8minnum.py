'''Question 16: Write a java program to find a minimum between three numbers.
Asked In Just Practice assignment
Input:
Number1 = 9
Number2 = 4
Number3 = 7

Output
Minimum number = 4'''
a=int(input("Enter number 1\n"))
b=int(input("Enter number 2\n"))
c=int(input("Enter number 3\n"))

if a<b and a<c:
    print("Minimum number =",a)
elif b<c:
    print("Minimum number =",b)
else:
    print("Minimum number =",c)