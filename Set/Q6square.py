'''6.Find the Square of Each Element
Write a Python program to create a set of integers and create a new set containing the square of 
each element.'''
n=int(input("Enter values size"))
s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
    '''
s1=set() 
for val in s:
    sq=val*val
    s1.add(sq)
print(s1)
'''
list=[]
for val in s:
    sq=val*val
    list.append(sq)
    
print(list)
    
