'''18. Find the maximum and minimum value in a tuple.'''

n=int(input("Enter tuple size"))
a=()
for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
mx=a[0]
mn=a[0]

for i in range(n):
    if a[i]>mx:
        mx=a[i]
    elif a[i]<mn:
        mn=a[i]
        
print("Maximum element ",mx)
print("Minimum element ",mn)