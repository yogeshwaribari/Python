'''Question 13: Write a java program to display only non-zero values from an array.
Asked In Practice assignment
Input : Array = {1, 0, 5, 0, 7, 0, 9}
Output : Non-zero elements = {1, 5, 7, 9}
Explanation :
Traverse the array and print only elements that are not equal to zero.'''

list=input("Enter elements in array").split()

for i in range(len(list)):
    list[i]=int(list[i])
    
for i in range(len(list)):
    if list[i]!=0:
      print(list[i],end=" ")
        