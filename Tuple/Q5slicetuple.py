'''5. Slice a tuple to print elements from index 1 to 4.'''

n=int(input("Enter values size"))
a=()

for i in range(n):
    x=int(input("Enter values"))
    a=a+(x,)
    
b=a[1:4]
print(b)