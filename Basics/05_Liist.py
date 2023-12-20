# list is a collections of items

marks = [10, 20, 30, "last"]

marks[1] = 99

print(marks)
print(marks[2])
print(marks[-1]) # last index
print(marks[0:3]) # = [10, 20, 30] --> Not print 3rd index

marks.insert(0, 0)
marks.append(0)

for i in marks:
    print(i)

print(0 in marks)
print(len(marks))