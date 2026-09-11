#Date: 11th September 2026
#Topics covered: Type Casting

'''
TYPECASTING

CONVERT THE STRING "100" INTO AN INTEGER.
CONVERT THE INTEGER 50 INTO A FLOAT.
CONVERT THE INTEGER 100 INTO A STRING.
CONVERT THE STRING "25.75" INTO A FLOAT.
TAKE TWO NUMBERS FROM THE USER AND PERFORM ADDITION AFTER CONVERTING THEM TO INTEGERS.
TAKE THE USER'S AGE AS INPUT AND CONVERT IT INTO AN INTEGER.
TAKE A DECIMAL NUMBER AS INPUT AND CONVERT IT INTO AN INTEGER. OBSERVE THE RESULT.
TAKE AN INTEGER AS INPUT, CONVERT IT INTO A FLOAT, AND PRINT ITS TYPE. '''

a = "100"
a = int(a)
print(a)

b = 50
b = float(b)
print(b)

c = 100
c = str(c)
print(c)

d = "25.75"
d = float(d)
print(d)

num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
print(num1 + num2)

age = input("ENTER AGE: ")
age = int(age)
print(age)

decimal_num = float(input("ENTER DECIMAL NUMBER: "))
decimal_num = int(decimal_num)
print(decimal_num)

n = int(input("ENTER AN INTEGER: "))
n = float(n)
print(type(n))
