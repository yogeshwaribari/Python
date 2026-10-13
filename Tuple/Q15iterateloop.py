'''15. Iterate through a tuple using a for loop.'''

n=int(input("Enter tuple size"))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
for i in a:
    print(i)