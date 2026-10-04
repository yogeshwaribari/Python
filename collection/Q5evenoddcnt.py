'''Question 5: Write a Java program to count even & odd values from an array.
Asked In Practice assignment
Input:
Array Size = 7
Array Elements = 12 17 24 39 40 55 70
Output:
Count of Even Values = 4
Count of Odd Values = 3
Explanation:
? Initialize counters: evenCount = 0, oddCount = 0.
? For each element in the array:
? If divisible by 2 ? increase evenCount.
? Otherwise ? increase oddCount.
? Final counts are displayed.
'''
n=int(input("Enter Array Size\n"))
list=[0]*n
ecnt=0
ocnt=0
print("Enter Array Elements")
for i in range(n):
    list[i]=int(input())

for i in range(n):
    if list[i]%2==0:
        ecnt+=1
    else:
        ocnt+=1
        
print("Count of Even Values = ",ecnt)
print("Count of Odd Values = ",ocnt)