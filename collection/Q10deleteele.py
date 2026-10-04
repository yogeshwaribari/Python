'''Question 10: Write a program in java to delete an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 5

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to delete : 3

Expected Output : The new list is : 1 2 3 5'''
n=int(input("Enter Size of array\n"))

list=[0]*n
print("Enter Array elements")
for i in range(n):
    list[i]=input()

p=int(input("Enter Position to delete element"))
for i in range(p-1,n-1):
    list[i]=list[i+1]
    
list.pop()
print(list)