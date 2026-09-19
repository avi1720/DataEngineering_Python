#Date: 19th September 2026

""" PYTHON TERNARY OPERATOR

BASIC

1. Take a number from the user and print "Even" if it is even, otherwise "Odd".
2. Take a number and print "Positive" if it is greater than 0, otherwise "Negative".
3. Take a number and print "Zero" if it is 0, otherwise "Non-zero".
4. Take a person's age and print "Adult" if age is 18 or above, otherwise "Minor".
5. Take a number and print "Greater than 50" if it is greater than 50, otherwise "50 or less".
6. Take two numbers and print the larger number using a ternary operator.
7. Take two numbers and print the smaller number using a ternary operator.
8. Take a student's mark and print "Pass" if the mark is 40 or above, otherwise "Fail".
9. Take a number and print "Divisible by 5" if it is divisible by 5, otherwise "Not divisible by 5".
10. Take a number and print "Multiple of 10" or "Not a multiple of 10".""" 

num = int(input())
print("Even" if num % 2 == 0 else "Odd")

num = int(input())
print("Positive" if num > 0 else "Negative")

num = int(input())
print("Zero" if num == 0 else "Non-zero")

age = int(input())
print("Adult" if age >= 18 else "Minor")

num = int(input())
print("Greater than 50" if num > 50 else "50 or less")

a = int(input())
b = int(input())
print(a if a > b else b)

a = int(input())
b = int(input())
print(a if a < b else b)

mark = int(input())
print("Pass" if mark >= 40 else "Fail")

num = int(input())
print("Divisible by 5" if num % 5 == 0 else "Not divisible by 5")

num = int(input())
print("Multiple of 10" if num % 10 == 0 else "Not a multiple of 10")

""" INTERMEDIATE

11. Take two numbers and print whether they are equal or not equal.
12. Take a person's age and print:
    • "Child" if age < 13
    • "Teenager" otherwise
13. Take a number and print "Positive Even" or "Not Positive Even".
14. Take two numbers and print the maximum using a ternary operator.
15. Take three numbers and find the largest number using nested ternary operators.
16. Take three numbers and find the smallest number using nested ternary operators.
17. Take a student's mark and display:
    • "Pass" if ≥ 40
    • "Fail" otherwise
18. Take a temperature and print:
    • "Hot" if temperature > 30
    • "Normal" otherwise
19. Take a salary and print:
    • "High Salary" if salary ≥ 50,000
    • "Low Salary" otherwise
20. Take a number and determine whether it is even and positive using a ternary operator. """

a = int(input())
b = int(input())
print("Equal" if a == b else "Not Equal")

age = int(input())
print("Child" if age < 13 else "Teenager")

num = int(input())
print("Positive Even" if num > 0 and num % 2 == 0 else "Not Positive Even")

a = int(input())
b = int(input())
print(a if a > b else b)

a = int(input())
b = int(input())
c = int(input())
print(a if a > b and a > c else b if b > c else c)

a = int(input())
b = int(input())
c = int(input())
print(a if a < b and a < c else b if b < c else c)

marks = int(input())
print("Pass" if marks >= 40 else "Fail")

temp = int(input())
print("Hot" if temp > 30 else "Normal")

salary = int(input())
print("High Salary" if salary >= 50000 else "Low Salary")

num = int(input())
print("Even and Positive" if num > 0 and num % 2 == 0 else "Not Even and Positive")

""" OUTPUT PREDICTION

Predict the output without executing the code.

21.
x = 10
result = "Yes" if x > 5 else "No"
print(result)

22.
x = 3
result = "Even" if x % 2 == 0 else "Odd"
print(result)

23.
age = 17
print("Adult" if age >= 18 else "Minor")

24.
a = 25
b = 15
print(a if a > b else b)

25.
marks = 35
print("Pass" if marks >= 40 else "Fail")

CONVERT IF-ELSE TO TERNARY

26. Convert this into a ternary operator:

age = 20

if age >= 18:
    result = "Eligible"
else:
    result = "Not Eligible"

27. Convert:

num = 7

if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"

28. Convert:

a = 10
b = 20

if a > b:
    result = a
else:
    result = b

29. Convert:

marks = 75

if marks >= 50:
    result = "Pass"
else:
    result = "Fail"

30. Convert:

num = -5

if num >= 0:
    result = "Positive"
else:
    result = "Negative" """

""" 21. Yes
    22. Odd
    23. Minor
    24. 25
    25. Fail 
result = "Eligible" if age >= 18 else "Not Eligible"
result = "Even" if num % 2 == 0 else "Odd"
result = a if a > b else b
result = "Pass" if marks >= 50 else "Fail"
result = "Positive" if num >= 0 else "Negative""""

""" CHALLENGE

31. Find the largest of three numbers using nested ternary operators.
32. Find the smallest of three numbers using ternary operators.
33. Check whether a number is positive, negative, or zero using nested ternary operators.
34. Take a student's mark and display:
    "Distinction" if ≥ 75,
    otherwise "Pass" if ≥ 40,
    otherwise "Fail".

35. Take a person's age and display:
    Child, Teenager, Adult, or Senior Citizen using nested ternary operators."""

a = int(input())
b = int(input())
c = int(input())
print(a if a > b and a > c else b if b > c else c)

a = int(input())
b = int(input())
c = int(input())
print(a if a < b and a < c else b if b < c else c)

num = int(input())
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

marks = int(input())
print("Distinction" if marks >= 75 else "Pass" if marks >= 40 else "Fail")

age = int(input())
print("Child" if age < 13 else "Teenager" if age < 20 else "Adult" if age < 60 else "Senior Citizen")

