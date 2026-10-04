'''Question 2: Write a Java program to calculate the sum of all elements in an array.
Asked In Practice assignment
Input:
Array Size = 5
Array Elements = 2 4 6 8 10
Output:
Sum of array elements = 30
Explanation:
? Initialize a variable sum = 0.
? Traverse the array and keep adding each element to sum.
? After the loop ends, sum will hold the total of all array elements.'''
n=int(input("Enter Array Size\n"))
list=[0]*n

print("Enter Array Elements")
for i in range(n):
    list[i]=int(input())
sum=0
for i in range(n):
    sum=sum+list[i]
   
print("Sum of array element =",sum)