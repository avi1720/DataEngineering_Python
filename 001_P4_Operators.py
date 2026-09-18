#Date: 14th September 2026
#Topic Covered: Operators

""" ARITHMETIC OPERATORS

1. Take two numbers and perform:
   • Addition
   • Subtraction
   • Multiplication
   • Division
   • Floor Division
   • Modulus
   • Exponentiation

2. Calculate the area and perimeter of a rectangle.
3. Calculate the total and average of three numbers.
4. Calculate the simple interest using:
   SI = (P * R * T) / 100
5. Convert Celsius to Fahrenheit.
6. Take a number and calculate its square and cube.
7. Take two numbers and find the remainder when the first number is divided by the second."""


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)
print("Area:", area)
print("Perimeter:", perimeter)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

total = a + b + c
average = total / 3
print("Total:", total)
print("Average:", average)

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


num = float(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Remainder:", a % b)

""" ASSIGNMENT OPERATORS

1. Create x = 10 and use += to increase it by 5.
2. Create x = 20 and use -= to decrease it by 7.
3. Create x = 5 and use *= to multiply it by 4.
4. Create x = 20 and use /= to divide it by 5.
5. Create x = 17 and use //= with 3.
6. Create x = 10 and use %= with 3.
7. Create x = 2 and use **= with 3.
8. Start with x = 100 and perform at least five different assignment operations. """

x = 10
x += 5
print(x)

x = 20
x -= 7
print(x)

x = 5
x *= 4
print(x)

x = 20
x /= 5
print(x)

x = 17
x //= 3
print(x)

x = 10
x %= 3
print(x)

x = 2
x **= 3
print(x)

x = 100
x += 20
x -= 10
x *= 2
x //= 3
x %= 5
print(x)

""" COMPARISON OPERATORS

1. Take two numbers and check whether they are equal.
2. Check whether the first number is greater than the second.
3. Check whether the first number is smaller than the second.
4. Check whether two user-entered numbers are different.
5. Take a student's mark and check whether it is greater than or equal to 50.
6. Take a person's age and check whether they are 18 or above.
7. Compare two strings using == and !=. """

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a == b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a > b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a < b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a != b)

mark = int(input("Enter mark: "))
print(mark >= 50)

age = int(input("Enter age: "))
print(age >= 18)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1 == s2)
print(s1 != s2)

"""
LOGICAL OPERATORS

1. Take age as input and check whether the person is between 18 and 60 using and.
2. Check whether a number is either less than 10 or greater than 100 using or.
3. Take a number and check whether it is not equal to 0 using not.
4. Check whether a student has passed both subjects:
   • Maths ≥ 40
   • Science ≥ 40
5. Check whether a person can vote using:
   • Age ≥ 18
   • Citizen = True
6. Check whether a number is between 10 and 50 using logical operators. """

age = int(input("Enter age: "))
print(age >= 18 and age <= 60)

num = int(input("Enter number: "))
print(num < 10 or num > 100)

num = int(input("Enter number: "))
print(not (num == 0))

maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
print(maths >= 40 and science >= 40)

age = int(input("Enter age: "))
citizen = input("Enter citizen status (True/False): ") == "True"
print(age >= 18 and citizen)

num = int(input("Enter number: "))
print(num >= 10 and num <= 50)

"""
BITWISE OPERATORS

Use the values a = 10 and b = 6.
1. Find the result of a & b.
2. Find the result of a | b.
3. Find the result of a ^ b.
4. Find the result of ~a.
5. Take two integers from the user and perform &, |, and ^.
6. Take a number from the user and apply the ~ operator.
7. Predict the output before executing:
   print(5 & 3)
8. Predict the output:
   print(5 | 3)
9. Predict the output:
   print(5 ^ 3)
10. Predict the output:
    print(~5) """

a = 10
b = 6
print(a & b)

a = 10
b = 6
print(a | b)

a = 10
b = 6
print(a ^ b)

a = 10
print(~a)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a & b)
print(a | b)
print(a ^ b)

num = int(input("Enter number: "))
print(~num)

print(5 & 3)

print(5 | 3)

print(5 ^ 3)

print(~5)
