'''16. Iterate through a tuple using a while loop.'''

n=int(input("Enter tuple size"))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
i=0  
while i<n:
    print(a[i])
    i=i+1