'''7. Count how many times a specific value appears in a tuple.'''

n=int(input("Enter values size "))
a=()

for i in range(n):
    x=int(input("Enter values "))
    a=a+(x,)
#count method
'''
num=int(input("Enter count number"))
c=a.count(num)

print(c)
'''
#without count method
num=int(input("Enter count number "))
cnt=0
for i in range(n):
    if a[i]==num:
        cnt+=1
print(cnt)