'''Question 12: Write a program in java to insert an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 6

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to insert : 2
Value : 200

Expected Output : The new list is : 1 2 200 3 4 5
'''
n=int(input("Enter array size"))
list=[0]*n
print("Enter 5 element in the array ")
for i in range(n-1):
    list[i]=int(input())
    
p=int(input("Enter position where to insert"))
val=int(input("Enter value"))
for i in range(n-1,p-1,-1):
    list[i]=list[i-1]
list[p]=val
    
print("New array = ",list)