'''9.Find the Product of All Elements
Write a Python program to create a set of integers and calculate the product of all elements.'''
#s={1,2,3,4,5}
n=int(input("Enter values size "))
s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
pro=1
for i in s:
    pro*=i
    
print("Product = ",pro)