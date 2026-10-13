'''19. Create a tuple of numbers and calculate their sum.'''

n=int(input("Enter tuple size "))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
s=0
for i in range(n):
    s=s+a[i]
    
print("Sum = ",s)