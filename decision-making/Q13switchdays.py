'''Question 55: Develop a Java program using switch to print the day type for an input day number 
(1-7):
? 1 for Monday, …, 7 for Sunday.
? For 1-5, display “Weekday”; for 6-7, display “Weekend”.
Asked In Just Practice assignment
Input:
Day = 3

Output:
Weekday

Explanation:
Day numbers 1 to 5 represent Monday to Friday, so they are weekdays.

Input:
Day = 7

Output:
Weekend'''

d=int(input("Enter days\n"))
match d:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Wrong choice")



