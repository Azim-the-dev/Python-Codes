num = 123
temp = 0
sum = 0

while (num != 0):
    temp = num % 10
    sum += temp

    num = num / 10

print(sum)