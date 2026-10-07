'''1. Find the Sum of All Elements in a Set
Write a Python program to create a set of integers and calculate the sum of all elements.'''
'''
a=set()
a.add(10)
a.add(20)
a.add(30)
a.add(40)
a.add(50)

a={10,20,30,40,50}
sum=0
for val in a:
    sum=sum+val
print("Sum all elements = ",sum)
'''

#user input
a=set(input("Enter elements = ").split())
sum=0
for val in a:
    sum=sum+int(val)
print("Sum all elements = ",sum)