'''10. Concatenate two tuples.'''

n=int(input("Enter tuple 1 size "))
a=()
for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
n1=int(input("Enter tuple 2 size "))
b=()
for i in range(n1):
    x=int(input("Enter values "))
    b=b+(x,)
    
c=a+b   #concatenate use '+' operator
print(c)
