'''3.Access the third element of a tuple.'''

n=int(input("Enter values size"))
a=()
for i in range(n):
    x=int(input("Enter values"))
    a=a+(x,)
print(a[2])
