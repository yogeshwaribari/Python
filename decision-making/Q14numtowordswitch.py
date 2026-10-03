'''Question 57: Create a Java program using switch to convert a given number (1-5) to its word equivalent (One, Two, ..., Five). If the number is not between 1 and 5, display “Invalid number”.
Asked In Just Practice assignment
Input:
Number = 3

Output:
Three

Explanation:
Switch case 3 matches and prints “Three”. Default handles invalid numbers.

Input:
Number = 9

Output:
Invalid Number
Explanation:
Since 9 is outside 1–5, default case runs.'''
num=int(input("Enter number 1 to 5\n"))
match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid number")