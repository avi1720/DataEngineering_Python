#Date: 18th September 2026

""" WHILE LOOP

1. Basic while Loop

1. Print the word "Python" 5 times using a while loop.
2. Print numbers from 25 down to 15.
3. Print every third number starting from 3 up to 30.
4. Print numbers from 2 to 40, increasing by 2 each time.
5. Print the first 10 multiples of 4.
6. Print numbers from 100 down to 50, decreasing by 5.
7. Print the numbers 1, 4, 7, 10, 13, ... up to 40.
8. Print the first 8 powers of 2 using a while loop. """

count = 1
while count <= 5:
    print("Python")
    count += 1

num = 25
while num >= 15:
    print(num)
    num -= 1

num = 3
while num <= 30:
    print(num)
    num += 3

num = 2
while num <= 40:
    print(num)
    num += 2

count = 1
while count <= 10:
    print(4 * count)
    count += 1

num = 100
while num >= 50:
    print(num)
    num -= 5

num = 1
while num <= 40:
    print(num)
    num += 3

count = 0
value = 1
while count < 8:
    print(value)
    value *= 2
    count += 1

""" 2. User Input + while

9. Keep asking the user to enter a number until they enter 0.
10. Keep asking the user to enter a password until they enter the correct password.
11. Ask the user to enter numbers continuously and stop when they enter -1.
12. Keep accepting numbers and display each number until the user enters 100.
13. Ask the user to enter a positive number. Continue asking until they enter a positive value.
14. Ask the user to enter "yes" or "no". Continue asking until either valid response is entered.
15. Ask the user to enter a number between 1 and 10. Keep asking until the input is within the range. """ 

password = "admin"
pwd = ""
while pwd != password:
    pwd = input("Enter password: ")

num = int(input("Enter number: "))
while num != 0:
    num = int(input("Enter number: "))

num = int(input("Enter number: "))
while num != -1:
    num = int(input("Enter number: "))

num = int(input("Enter number: "))
while num != 100:
    print(num)
    num = int(input("Enter number: "))

num = int(input("Enter a positive number: "))
while num <= 0:
    num = int(input("Enter a positive number: "))

text = input("Enter yes or no: ")
while text.lower() not in ["yes", "no"]:
    text = input("Enter yes or no: ")

num = int(input("Enter a number between 1 and 10: "))
while num < 1 or num > 10:
    num = int(input("Enter a number between 1 and 10: "))

""" 3. Calculations Using while

16. Find the sum of the first 20 natural numbers using while.
17. Find the sum of numbers entered by the user until the user enters 0.
18. Calculate the product of numbers from 1 to 10.
19. Calculate the average of numbers entered by the user until -1 is entered.
20. Count how many numbers the user enters before entering 0.
21. Find the largest value from numbers entered continuously until -1.
22. Find the smallest value from numbers entered continuously until -1.
23. Calculate the running total as the user enters numbers. """

total = 0
num = 1
while num <= 20:
    total += num
    num += 1
print(total)

total = 0
num = int(input("Enter number: "))
while num != 0:
    total += num
    num = int(input("Enter number: "))
print(total)

product = 1
num = 1
while num <= 10:
    product *= num
    num += 1
print(product)

total = 0
count = 0
num = int(input("Enter number: "))
while num != -1:
    total += num
    count += 1
    num = int(input("Enter number: "))
print(total / count)

count = 0
num = int(input("Enter number: "))
while num != 0:
    count += 1
    num = int(input("Enter number: "))
print(count)

largest = float("-inf")
num = int(input("Enter number: "))
while num != -1:
    if num > largest:
        largest = num
    num = int(input("Enter number: "))
print(largest)

smallest = float("inf")
num = int(input("Enter number: "))
while num != -1:
    if num < smallest:
        smallest = num
    num = int(input("Enter number: "))
print(smallest)

total = 0
num = int(input("Enter number: "))
while num != 0:
    total += num
    print(total)
    num = int(input("Enter number: "))



""" 4. Number-Based Problems

24. Count the number of digits in an integer using while.
25. Extract and print each digit of a number separately.
26. Find the first digit of a number using a while loop.
27. Find the sum of all digits of a number.
28. Find the product of all digits of a number.
29. Reverse an integer using while.
30. Count how many times a particular digit occurs in a number.
31. Find the largest digit in a number.
32. Find the smallest digit in a number.
33. Remove the last digit of a number repeatedly and display the intermediate values. """

num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

num = int(input("Enter number: "))
while num > 0:
    print(num % 10)
    num //= 10

num = int(input("Enter number: "))
temp = num
while temp >= 10:
    temp //= 10
print(temp)

num = int(input("Enter number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)

num = int(input("Enter number: "))
product = 1
while num > 0:
    product *= num % 10
    num //= 10
print(product)

num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

num = int(input("Enter number: "))
digit = int(input("Enter digit: "))
count = 0
while num > 0:
    if num % 10 == digit:
        count += 1
    num //= 10
print(count)

num = int(input("Enter number: "))
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10
print(largest)

num = int(input("Enter number: "))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //= 10
print(smallest)

num = int(input("Enter number: "))
while num > 0:
    num //= 10
    print(num)

""" 5. Menu-Driven Programs

34. Create a menu that repeatedly displays:

1. Add
2. Subtract
3. Exit

Continue until the user selects Exit.

35. Create a simple bank menu:

1. Check Balance
2. Deposit
3. Withdraw
4. Exit

Use a while loop to keep the menu running.

36. Create a shopping menu:

1. Add Item
2. View Total
3. Clear Cart
4. Exit

37. Create a student menu:

1. Enter Marks
2. Display Marks
3. Calculate Total
4. Exit

38. Create a calculator that continues accepting operations until the user chooses "Exit". """

choice = 0
while choice != 3:
    print("1.Add")
    print("2.Subtract")
    print("3.Exit")
    choice = int(input("Enter choice: "))

balance = 1000
choice = 0
while choice != 4:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print(balance)
    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance += amount
    elif choice == 3:
        amount = float(input("Enter amount: "))
        balance -= amount

total = 0
choice = 0
while choice != 4:
    print("1.Add Item")
    print("2.View Total")
    print("3.Clear Cart")
    print("4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        price = float(input("Enter price: "))
        total += price
    elif choice == 2:
        print(total)
    elif choice == 3:
        total = 0

marks = []
choice = 0
while choice != 4:
    print("1.Enter Marks")
    print("2.Display Marks")
    print("3.Calculate Total")
    print("4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        marks.append(int(input("Enter mark: ")))
    elif choice == 2:
        print(marks)
    elif choice == 3:
        print(sum(marks))

choice = ""
while choice.lower() != "exit":
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    choice = input("Type Exit to quit or Enter to continue: ")

""" 6. while with Conditions

39. Start with a number and repeatedly subtract 7 until the value becomes less than 0.
40. Start with x = 1 and repeatedly multiply it by 3 until it becomes greater than 500.
41. Take a number and repeatedly divide it by 2 until it becomes 0.
42. Keep generating numbers starting from 1 and stop when the sum becomes greater than 100.
43. Generate consecutive numbers and stop when you encounter a number divisible by both 4 and 6.
44. Start with a user's balance and repeatedly deduct a fixed expense until the balance becomes insufficient. """

num = int(input("Enter number: "))
while num >= 0:
    print(num)
    num -= 7

x = 1
while x <= 500:
    print(x)
    x *= 3

num = int(input("Enter number: "))
while num > 0:
    print(num)
    num //= 2

num = 1
total = 0
while total <= 100:
    total += num
    print(num)
    num += 1

num = 1
while True:
    print(num)
    if num % 4 == 0 and num % 6 == 0:
        break
    num += 1

balance = float(input("Enter balance: "))
expense = float(input("Enter expense: "))
while balance >= expense:
    balance -= expense
    print(balance)

""" 7. Nested while Loop

45. Print a 3 × 4 grid of numbers using nested while loops.
46. Print this pattern using nested while loops:

1 2 3
4 5 6
7 8 9

47. Print a multiplication table grid from 1 to 5 using nested while loops.
48. Print this pattern:

A B C
A B C
A B C
A B C

49. Generate a simple number matrix where the user enters the number of rows and columns."""

row = 1
while row <= 3:
    col = 1
    while col <= 4:
        print(col, end=" ")
        col += 1
    print()
    row += 1

row = 0
num = 1
while row < 3:
    col = 0
    while col < 3:
        print(num, end=" ")
        num += 1
        col += 1
    print()
    row += 1

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1

row = 1
while row <= 4:
    col = 65
    while col <= 67:
        print(chr(col), end=" ")
        col += 1
    print()
    row += 1

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

i = 1
while i <= rows:
    j = 1
    while j <= cols:
        print(j, end=" ")
        j += 1
    print()
    i += 1

""" 8. Real-World Problems

50. ATM PIN System
Allow the user a maximum of 3 attempts to enter a PIN. Display an appropriate message after each attempt.

51. Parking Counter
Start with 20 available parking spaces. Each time a vehicle enters, reduce the available count. Stop when no spaces remain.

52. Countdown Timer Logic
Take a number of seconds and count down to zero using a while loop.

53. Savings Tracker
Ask the user for monthly savings and continue adding them until the total savings reach ₹1,00,000.

54. Login Attempts
Allow a user to enter their username and password. Give them a maximum of 3 attempts.

55. Guess the Number
Store a secret number and repeatedly ask the user to guess until they find it.

56. Digital Wallet
Start with a wallet balance. Allow the user to make purchases repeatedly until the balance is insufficient or they choose to stop.""" 

attempts = 0
pin = "1234"

while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
    attempts += 1

spaces = 20
while spaces > 0:
    input("Vehicle Entered. Press Enter...")
    spaces -= 1
    print("Available Spaces:", spaces)

seconds = int(input("Enter seconds: "))
while seconds >= 0:
    print(seconds)
    seconds -= 1

total = 0
while total < 100000:
    savings = float(input("Enter monthly savings: "))
    total += savings
print(total)

username = "admin"
password = "1234"
attempts = 0

while attempts < 3:
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Login Successful")
        break

    attempts += 1

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess: "))

balance = float(input("Enter wallet balance: "))

while balance > 0:
    amount = float(input("Purchase amount: "))
    if amount > balance:
        print("Insufficient balance")
        break
    balance -= amount
    print("Balance:", balance)

    choice = input("Continue? (yes/no): ")
    if choice.lower() != "yes":
        break

""" 9. Challenge Problems

57. Convert a decimal number to binary using a while loop.
58. Convert a binary number entered by the user into a decimal number using a while loop.
59. Check whether a number is a palindrome using while.
60. Generate the Collatz sequence:

• If the number is even → divide by 2
• If the number is odd → multiply by 3 and add 1
• Continue until the number becomes 1

61. Find the GCD of two numbers using a while loop.
62. Find the LCM of two numbers using a while loop.
63. Implement a simple number guessing game that also counts the number of attempts.
64. Create a program that repeatedly asks for a number and displays its digits in reverse order until the user chooses to stop."""

num = int(input("Enter decimal number: "))
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print(binary)

binary = int(input("Enter binary number: "))
decimal = 0
base = 1

while binary > 0:
    digit = binary % 10
    decimal += digit * base
    base *= 2
    binary //= 10

print(decimal)

num = int(input("Enter number: "))
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

num = int(input("Enter number: "))

while num != 1:
    print(num, end=" ")
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

print(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print(a)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        print(lcm)
        break
    lcm += 1

secret = 8
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess == secret:
        print("Attempts:", attempts)
        break

choice = "yes"

while choice.lower() == "yes":
    num = int(input("Enter number: "))
    rev = 0
    temp = num

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    print(rev)
    choice = input("Continue? (yes/no): ")


