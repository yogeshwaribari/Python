'''Question 8: Write a java program to find missing elements in an array.
Asked In Practice assignment
Input : Array = {1, 2, 4, 5, 7} (numbers from 1 to 7 should be present)
Output : Missing elements = {3, 6}
Explanation:
Check sequence numbers one by one. If a number from 1 to maximum (7) is not in the array,
 it is missing.'''
 
#list=[1,2,4,5,7]
 
n=int(input("Enter array size"))
list=[0]*n
print("Enter array elements")
for i in range(n):
     list[i]=int(input())
     
for i in range(1,max(list)+1):
    flag=False
    for j in range(len(list)):
        if list[j]==i:
            flag=True
            break
            
    if flag==False:
        print(i,end=" ")
   
        
 