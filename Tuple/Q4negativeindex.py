'''4. Print the last element of a tuple using negative indexing.'''

n=int(input("Enter values Size"))
a=()

for i in range(n):
    x=int(input("Enter values"))
    a=a+(x,)
    
print(a[-1])