# Input Output
print("\n")
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Type Conversion 
print("\n")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sum = int(num1) + int(num2)
print("Sum is: ", sum)

# Strings
print("\n")
print(name.upper())
print(name.lower())
print(name.find('A'))
print(name.replace("Azim", "Hello, Azim"))
print('A' in name)
print(name[0])
# name[0] = Z --> Can not do this
print(name[0:2])

# logical Operators
print("\n")
print((2 == 2))
print(not (2 == 2))
print((2 == 2) or (2 == 5))
print((2 == 2) and (2 == 5))

# If-Else
print("\n")
age = input("Enter your age: ")

if (int(age) > 18):
    print("You are an adult !")
elif ((int(age) < 18) and int(age) > 3):
    print("You are in school !")
else:
    print("You are a KID !")

# Range
print("\n")
numbers = range(5) # = 0,1,2,3,4
print(numbers)

# Loops
i = 1
while (i <= 10):
    print(i)
    i += 1

for J in range(5):
    print(J)