'''9. Check if an element exists in a tuple.'''

n=int(input("Enter element size "))
a=()
for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
num=int(input("Enter element "))

for i in range(n):
    if a[i]==num:
        print("Element exist")
        break
else:
    print("Element not exist")