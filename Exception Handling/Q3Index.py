'''Q3. List Index Error
Create a list of five numbers. Ask the user to enter an index and display the corresponding 
element. Handle an invalid index.
'''
list=[10,20,30,40,50]
n=int(input("Enter size of list "))
for i in range(n):
    list[i]=int(input("Enter values"))
    
try:
    inx=int(input("Enter index for display data "))
    #c=list.pop(inx)
    c=list[inx]
    print(c)
except IndexError as e:
    print("Index is Out of range")