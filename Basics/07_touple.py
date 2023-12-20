# touple are immutable

marks = (2, 22 ,33 ,55 ,55 ,66, 77, 55)

# marks[0] = 99 --> not work due to immutable

print(marks.count(55))
print(marks.index(33))