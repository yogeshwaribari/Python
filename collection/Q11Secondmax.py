'''Question 11: Write a java program to give an array, find the second largest element.
Asked In Practice assignment
Input : Array = {12, 35, 1, 10, 34, 1}
Output : Second largest = 34
Explanation:
First largest is 35, second largest is the next maximum (34). We maintain two variables
 (largest, secondLargest).'''
n=int(input("Enter Array Size\n"))
list=[0]*n
print("Enter Array element")
for i in range(n):
    list[i]=int(input())
    
max=list[0]
smax=list[1]
for i in range(n):
    if list[i]>max:
        smax=max
        max=list[i]
        
    elif max>list[i] and smax<list[i]:
        smax=list[i]
            
print("Second largest = ",smax)            