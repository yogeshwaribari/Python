'''12. Convert a list into a tuple.'''
'''
l=[10,20,30,40]
a=tuple(l)
print(a)
'''
n=int(input("Enter list size "))
list=[0]*n

for i in range(n):
    list[i]=input("Enter values ")
    
a=tuple(list)
print(a)