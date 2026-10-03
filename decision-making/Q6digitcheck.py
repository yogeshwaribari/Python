'''Question 10: Write a java program to input any character and check whether it is alphabet, 
digit or special character.
Asked In Just Practice assignment
Input:
Character = 5

Output:
Digit

Explanation:
Check ASCII ranges.'''
ch=input("Enter Character\n")

if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
    print("Alphabet")
elif (ch<"9") and (ch>"0"):
    print("Digit")
else:
    print("Special character")