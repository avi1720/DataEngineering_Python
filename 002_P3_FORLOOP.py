#Date: 19th September 2026

""" FOR LOOP

1. Basic for Loop

1. Print numbers from 1 to 10 using a for loop.
2. Print numbers from 10 to 1.
3. Print all numbers from 1 to 20.
4. Print all even numbers from 1 to 20.
5. Print all odd numbers from 1 to 20.
6. Print multiples of 5 from 5 to 50.
7. Print numbers from 20 to 50.
8. Print numbers from 100 to 110.
9. Print the first 10 natural numbers.
10. Print the first 10 whole numbers. """

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 21):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(1, 21, 2):
    print(i)

for i in range(5, 51, 5):
    print(i)

for i in range(20, 51):
    print(i)

for i in range(100, 111):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10):
    print(i)

""" 2. Using range()

11. Use range() to print numbers from 1 to 10.
12. Use range() to print even numbers from 2 to 20.
13. Use range() to print odd numbers from 1 to 19.
14. Print numbers from 10 to 50 with a step of 5.
15. Print numbers from 50 to 10 in descending order.
16. Print multiples of 3 from 3 to 30.
17. Print multiples of 7 from 7 to 70.
18. Print numbers from 1 to 100 with a step of 10. """

for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

for i in range(1, 20, 2):
    print(i)

for i in range(10, 51, 5):
    print(i)

for i in range(50, 9, -1):
    print(i)

for i in range(3, 31, 3):
    print(i)

for i in range(7, 71, 7):
    print(i)

for i in range(1, 101, 10):
    print(i)

""" 3. Arithmetic with for Loop

19. Print the square of numbers from 1 to 10.
20. Print the cube of numbers from 1 to 10.
21. Find the sum of numbers from 1 to 10.
22. Find the sum of numbers from 1 to 100.
23. Find the sum of all even numbers from 1 to 50.
24. Find the sum of all odd numbers from 1 to 50.
25. Print the multiplication table of 5.
26. Ask the user for a number and print its multiplication table from 1 to 10.
27. Ask the user for a number n and calculate the sum from 1 to n.
28. Find the factorial of a number using a for loop. """

for i in range(1, 11):
    print(i ** 2)

for i in range(1, 11):
    print(i ** 3)

total = 0
for i in range(1, 11):
    total += i
print(total)

total = 0
for i in range(1, 101):
    total += i
print(total)

total = 0
for i in range(2, 51, 2):
    total += i
print(total)

total = 0
for i in range(1, 51, 2):
    total += i
print(total)

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

""" 4. Conditions Inside for Loop

29. Print numbers from 1 to 50 that are divisible by 5.
30. Print numbers from 1 to 100 that are divisible by both 3 and 5.
31. Print numbers from 1 to 100 that are not divisible by 2.
32. Count how many even numbers exist between 1 and 100.
33. Count how many odd numbers exist between 1 and 100.
34. Find the largest number among numbers from 1 to 20.
35. Find the sum of numbers divisible by 3 between 1 and 100.
36. Print numbers between 1 and 100 that are divisible by 7 but not by 5. """

for i in range(1, 51):
    if i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 2 != 0:
        print(i)

count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
print(count)

count = 0
for i in range(1, 101):
    if i % 2 != 0:
        count += 1
print(count)

largest = 1
for i in range(1, 21):
    if i > largest:
        largest = i
print(largest)

total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print(total)

for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

""" 5. Strings with for Loop

37. Print each character of "PYTHON" on a separate line.
38. Count the number of characters in a string using a for loop.
39. Count the number of vowels in a string.
40. Count the number of consonants in a string.
41. Print only the vowels from a given string.
42. Print only the digits from a string such as "abc123xyz45".
43. Count how many times the letter "a" appears in a string.
44. Reverse a string using a for loop.
45. Print each character along with its position.""" 

for ch in "PYTHON":
    print(ch)

s = input()
count = 0
for i in s:
    count += 1
print(count)

s = input()
count = 0
for i in s.lower():
    if i in "aeiou":
        count += 1
print(count)

s = input()
count = 0
for i in s.lower():
    if i.isalpha() and i not in "aeiou":
        count += 1
print(count)

s = input()
for i in s:
    if i.lower() in "aeiou":
        print(i)

s = "abc123xyz45"
for i in s:
    if i.isdigit():
        print(i)

s = input()
count = 0
for i in s.lower():
    if i == "a":
        count += 1
print(count)

s = input()
rev = ""
for i in s:
    rev = i + rev
print(rev)

s = input()
pos = 1
for i in s:
    print(pos, i)
    pos += 1

""" 6. Pattern Programs """

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    print(str(i) * i)

for i in range(5):
    print("*" * 5)


""" 7. Nested for Loop

51. Print multiplication tables from 1 to 5.

52. Print numbers in this format:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

53. Print a 5 × 5 star pattern.
54. Print this pattern:

1 2 3
1 2 3
1 2 3
55. Print multiplication tables from 2 to 10. """

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    print(str(i) * i)

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

""" 8. User Input + for Loop

56. Ask the user for n and print numbers from 1 to n.
57. Ask the user for n and print all even numbers up to n.
58. Ask the user for n and print all odd numbers up to n.
59. Ask the user for n and calculate its factorial.
60. Ask the user for a number and print its multiplication table.
61. Ask the user for 5 numbers and calculate their sum.
62. Ask the user for 5 numbers and find the largest number.
63. Ask the user for 5 numbers and count how many are even.
64. Ask the user for 5 numbers and count how many are positive and negative. """

n = int(input())
for i in range(1, n + 1):
    print(i)

n = int(input())
for i in range(2, n + 1, 2):
    print(i)

n = int(input())
for i in range(1, n + 1, 2):
    print(i)

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

total = 0
for i in range(5):
    num = int(input())
    total += num
print(total)

largest = int(input())
for i in range(4):
    num = int(input())
    if num > largest:
        largest = num
print(largest)

count = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        count += 1
print(count)

positive = 0
negative = 0
for i in range(5):
    num = int(input())
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print("Positive:", positive)
print("Negative:", negative)

""" 9. Challenge Questions

65. Check whether a given number is prime using a for loop.
66. Find all prime numbers between 1 and 100.
67. Find the factors of a given number.
68. Find the sum of all factors of a number.
69. Check whether a number is a perfect number.
70. Print the Fibonacci series for n terms using a for loop.
71. Find the sum of digits of a number.
72. Reverse a number using a for loop.
73. Check whether a number is a palindrome.
74. Print all numbers between 1 and 100 that are divisible by their own digits where applicable.
75. Generate the following pattern:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 """

n = int(input())
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

n = int(input())
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print("Perfect" if total == n else "Not Perfect")

n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

n = int(input())
total = 0
for digit in str(n):
    total += int(digit)
print(total)

n = input()
rev = ""
for ch in n:
    rev = ch + rev
print(rev)

n = input()
rev = ""
for ch in n:
    rev = ch + rev
print("Palindrome" if n == rev else "Not Palindrome")

for num in range(1, 101):
    valid = True
    for digit in str(num):
        if digit == '0' or num % int(digit) != 0:
            valid = False
            break
    if valid:
        print(num)

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

