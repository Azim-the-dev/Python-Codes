# Write a Program to display the first n terms of Fibonacci series.

def fib(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

# main
num = int(input("Enter number of terms: "))

for i in range(num):
    print(fib(i))