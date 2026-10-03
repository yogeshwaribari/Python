'''Question 19: Given a score out of 100, print Excellent (?90), Good (?75), Average (?50), 
Poor (< 50) — using nested ternary operators.
Asked In Just Practice assignment
Input:
Score = 82

Output:
Good

Explanation:
82 is greater than 75 but less than 90, so the grade is "Good".
Nested ternary operators are used instead of multiple if-else statements.'''
s=int(input("Enter score\n"))
if s>=90 and s<=100:
    print("Excellent")
elif s>=75:
    print("Good")
elif s>=50:
    print("Average")
else:
    print("Poor")