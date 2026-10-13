'''20. Unpack a tuple into different variables.'''
n=int(input("Enter tuple size"))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
    
b,c,d,*e=a
print(b,"\t",c,"\t",d,"\t",e)