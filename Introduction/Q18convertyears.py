'''Question 18: Write a Java program to convert days into years, months, and weeks.
Asked In Basic program
Input:
Days = 400

Output:
Years = 1
Months = 1
Weeks = 0

Explanation:
1 year = 365 days.
After subtracting 365 days, the remaining days are divided into months (30 days each) 
and weeks (7 days each).'''
day=int(input("Enter Days\n"))
y=day//365
rem=day%365
m=rem//30
rem=rem%30
w=rem//7

print("Years =",y)
print("Months =",m)
print("Weeks =",w)