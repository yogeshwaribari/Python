'''Question 17: Write a Java program to convert seconds into hours, minutes, and seconds.
Asked In Basic program
Input:
Seconds = 3665

Output:
Hours = 1
Minutes = 1
Seconds = 5

Explanation:
1 hour = 3600 seconds.
3665 / 3600 gives 1 hour.
Remaining seconds are converted into minutes and seconds using division and modulus operations.'''
sec=int(input("Enter Seconds\n"))
h=sec//3600
rem=sec%3600
min=rem//60
sec=rem%60

print("Hours =",h)
print("Minutes =",min)
print("Seconds =",sec)
