'''13. Convert a tuple into a list.'''
n=int(input("Enter tuple size "))
a=()
for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)

l=list(a)
print(l)