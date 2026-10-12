'''8. Find the index of a given element in a tuple.'''

n=int(input("Enter values size "))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
num=int(input("Enter value for index "))
'''
c=a.index(num)
print("index is ",c)
'''
for i in range(n):
    if a[i]==num:
        break
print(i)