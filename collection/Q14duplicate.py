'''Question 14: Write a java program to remove duplicated values from arrays.
Asked In Practice assignment
Input : Array = {10, 20, 20, 30, 40, 40, 50}
Output : Unique elements = {10, 20, 30, 40, 50}
Explanation:
Traverse the array, check if element already exists before adding to result, 
thus avoiding duplicates.'''
list=input("Enter elements array ").split()

for i in range(len(list)):
    list[i]=int(list[i])
    
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]!=list[j]:
            print(list[j],end=" ")
        