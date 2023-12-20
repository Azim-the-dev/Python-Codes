# Write a Program to find factorial of the given number.

def fac(num):
    if (num == 0):
        return 1
    else:
        return num * fac(num - 1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is:", fac(num))