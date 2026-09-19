#Date: 19th September 2026

""" 1. Python Conditions
1. Take a number from the user. Print "Positive" if the number is greater than 0.
2. Take a number and print "Even" if it is divisible by 2.
3. Take a person's age and print "Eligible to vote" if age is 18 or above.
4. Take a student's mark and print "Pass" if the mark is 40 or above.
5. Take a number and print "Greater than 100" if it is greater than 100.
6. Take a number and print "Divisible by 5" if it is divisible by 5.
7. Take a salary and print "High Salary" if salary is greater than 50,000.
8. Take a temperature and print "Hot" if the temperature is greater than 30.
9. Take a number and print "Multiple of 10" if it is divisible by 10.
10. Take a string and print "Python" if the entered string is "Python"."""

# 1
num = int(input())
if num > 0:
    print("Positive")

# 2
num = int(input())
if num % 2 == 0:
    print("Even")

# 3
age = int(input())
if age >= 18:
    print("Eligible to vote")

# 4
mark = int(input())
if mark >= 40:
    print("Pass")

# 5
num = int(input())
if num > 100:
    print("Greater than 100")

# 6
num = int(input())
if num % 5 == 0:
    print("Divisible by 5")

# 7
salary = int(input())
if salary > 50000:
    print("High Salary")

# 8
temp = int(input())
if temp > 30:
    print("Hot")

# 9
num = int(input())
if num % 10 == 0:
    print("Multiple of 10")

# 10
text = input()
if text == "Python":
    print("Python")


""" 2. If else condition
11. Take a number and check whether it is even or odd.
12. Take a number and check whether it is positive or negative.
13. Take a student's mark and display Pass or Fail.
14. Take a person's age and display Adult or Minor.
15. Take two numbers and print the greater number.
16. Take two numbers and check whether they are equal or not equal.
17. Take a number and check whether it is divisible by 5 or not.
18. Take a username from the user. If it is "admin", print "Welcome Admin", otherwise print "Invalid User".
19. Take a password from the user. If the password is "python123", print "Login Successful", otherwise print "Incorrect Password".
20. Take a student's attendance percentage. If it is 75 or above, print "Eligible for Exam", otherwise print "Not Eligible". """

# 11
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 12
num = int(input())
if num >= 0:
    print("Positive")
else:
    print("Negative")

# 13
mark = int(input())
if mark >= 40:
    print("Pass")
else:
    print("Fail")

# 14
age = int(input())
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 15
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# 16
a = int(input())
b = int(input())
if a == b:
    print("Equal")
else:
    print("Not Equal")

# 17
num = int(input())
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# 18
username = input()
if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid User")

# 19
password = input()
if password == "python123":
    print("Login Successful")
else:
    print("Incorrect Password")

# 20
attendance = float(input())
if attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible")

"""
3. IF-ELIF-ELSE CONDITION
21. Take a number and display:
• "Positive" if greater than 0
• "Negative" if less than 0
• "Zero" if equal to 0

22. Take a student's mark and display:
• A → 90–100
• B → 75–89
• C → 60–74
• D → 40–59
• F → Below 40

23. Take a person's age and display:
• "Child" → Below 13
• "Teenager" → 13–19
• "Adult" → 20–59
• "Senior Citizen" → 60 or above

24. Take a number and check whether it is:
• Positive Even
• Positive Odd
• Negative Even
• Negative Odd
• Zero

25. Take a temperature and display:
• "Cold" → Below 20
• "Normal" → 20–30
• "Hot" → Above 30

26. Take a month number and display the month name.
Example:
1 → January
2 → February
...
12 → December

27. Take a number from 1 to 7 and display the corresponding day.
1 → Monday
2 → Tuesday
...
7 → Sunday

28. Take a student's percentage and display:
• 90–100 → Distinction
• 75–89 → First Class
• 60–74 → Second Class
• 40–59 → Pass
• Below 40 → Fail

29. Take a person's age and calculate the ticket category:
• Below 5 → Free
• 5–12 → Child Ticket
• 13–59 → Adult Ticket
• 60+ → Senior Citizen Ticket

30. Take a number from the user and check whether it is:
• Less than 10
• Between 10 and 50
• Between 51 and 100
• Greater than 100 """

num = int(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


mark = int(input())

if mark >= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 40:
    print("D")
else:
    print("F")


age = int(input())

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


num = int(input())

if num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
elif num < 0 and num % 2 != 0:
    print("Negative Odd")
else:
    print("Zero")


temp = int(input())

if temp < 20:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")


month = int(input())

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")


day = int(input())

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")


percent = float(input())

if percent >= 90:
    print("Distinction")
elif percent >= 75:
    print("First Class")
elif percent >= 60:
    print("Second Class")
elif percent >= 40:
    print("Pass")
else:
    print("Fail")


age = int(input())

if age < 5:
    print("Free")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")


num = int(input())

if num < 10:
    print("Less than 10")
elif num <= 50:
    print("Between 10 and 50")
elif num <= 100:
    print("Between 51 and 100")
else:
    print("Greater than 100")

""" 4. NESTED CONDITIONS

31. Take a number. First check whether it is positive. If positive, check whether it is even or odd.
32. Take a student's mark. If the student has passed, check whether the mark is above 75.
33. Take age and citizenship status. Check whether the person is eligible to vote only when:
• Age ≥ 18
• Citizen = True

34. Take username and password. Check whether the username is correct first, then check the password.
35. Take three numbers and find the largest number using nested if conditions. """

num = int(input())

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")


mark = int(input())

if mark >= 40:
    if mark > 75:
        print("Passed and Above 75")
    else:
        print("Passed")
else:
    print("Failed")


age = int(input())
citizen = input()

if age >= 18:
    if citizen == "True":
        print("Eligible to Vote")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")


username = input()
password = input()

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")


a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

""" 5. REAL-WORLD MINI PROBLEMS

36. Electricity Bill
Take units consumed and calculate:
• 0–100 units → ₹2/unit
• 101–200 units → ₹3/unit
• 201–500 units → ₹5/unit
• Above 500 units → ₹7/unit
37. ATM Withdrawal
Take account balance and withdrawal amount. Check:
• Whether sufficient balance exists
• Whether withdrawal amount is valid
• Display the remaining balance
38. Login System
Take:
• Username
• Password
Check whether both are correct and display an appropriate message.
39. Calculator
Take two numbers and an operator:
• +
• -
• *
• /
Use if-elif-else to perform the operation.
40. Student Grade System
Take marks for three subjects, calculate the average, and display the grade using if-elif-else.""" 

units = int(input())

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 500:
    bill = units * 5
else:
    bill = units * 7

print(bill)


balance = float(input())
withdraw = float(input())

if withdraw > 0:
    if withdraw <= balance:
        print("Withdrawal Successful")
        print("Remaining Balance:", balance - withdraw)
    else:
        print("Insufficient Balance")
else:
    print("Invalid Withdrawal Amount")


username = input()
password = input()

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Username or Password")


num1 = float(input())
num2 = float(input())
op = input()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")


m1 = float(input())
m2 = float(input())
m3 = float(input())

avg = (m1 + m2 + m3) / 3

if avg >= 90:
    print("A")
elif avg >= 75:
    print("B")
elif avg >= 60:
    print("C")
elif avg >= 40:
    print("D")
else:
    print("F")
