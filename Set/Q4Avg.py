'''4. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements.
'''
n=int(input("Enter values size "))
s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
total=0
for val in s:
    total+=val
    
avg=total/len(s)
print("Average = ",avg)
    