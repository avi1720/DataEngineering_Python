#Date: 11th September 2026
#Topics Covered: User Input

""" USER INPUT

• ASK THE USER TO ENTER THEIR NAME AND PRINT A WELCOME MESSAGE.
• ASK THE USER TO ENTER THEIR AGE AND PRINT THEIR AGE.
• ASK THE USER TO ENTER TWO NUMBERS AND PRINT THEM.
• ASK THE USER TO ENTER THEIR NAME, AGE, AND CITY AND DISPLAY ALL THREE.
• ASK THE USER TO ENTER TWO NUMBERS AND CALCULATE THEIR SUM.
• ASK THE USER TO ENTER THE LENGTH AND BREADTH OF A RECTANGLE AND CALCULATE ITS AREA.
• ASK THE USER TO ENTER THE RADIUS OF A CIRCLE AND CALCULATE ITS AREA.
• ASK THE USER TO ENTER THEIR MARKS IN THREE SUBJECTS AND PRINT THE TOTAL. """

name = input("ENTER YOUR NAME: ")
print("WELCOME", name)

age = int(input("ENTER YOUR AGE: "))
print(age)

num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
print(num1, num2)

name = input("ENTER YOUR NAME: ")
age = int(input("ENTER YOUR AGE: "))
city = input("ENTER YOUR CITY: ")
print(name, age, city)

num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
print(num1 + num2)

length = float(input("ENTER LENGTH: "))
breadth = float(input("ENTER BREADTH: "))
print(length * breadth)

radius = float(input("ENTER RADIUS: "))
print(3.14 * radius * radius)

m1 = int(input("ENTER MARK 1: "))
m2 = int(input("ENTER MARK 2: "))
m3 = int(input("ENTER MARK 3: "))
print(m1 + m2 + m3)
