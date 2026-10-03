'''Question 3: Write a java program to print all alphabets from a to z. - using while loop
Asked In Just Practice assignment
Input:

No input required

Output:

a b c d e f ... z

Explanation:

The program starts from character ‘a’ and prints each character until ‘z’.
The loop increments the character in every iteration.'''

i="a"
while i<="z":
    print(i,end=" ")
    i=(chr)(ord(i)+1) #ord using for ascii value