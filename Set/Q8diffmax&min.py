'''8.Find the Difference Between Maximum and Minimum
Write a Python program to create a set of integers and calculate the difference between the 
maximum and minimum elements.'''

#s={10,20,30,40,50}
n=int(input("Enter values size "))
s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
mx=max(s)
mn=min(s)

diff=mx-mn
print("Maximum number = ",mx)
print("Minimum number = ",mn)
print("Difference between = ",diff)
