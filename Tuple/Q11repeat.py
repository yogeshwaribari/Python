'''11. Repeat a tuple 3 times.'''

n=int(input("Enter tuple size "))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
c=a*3
print(c)