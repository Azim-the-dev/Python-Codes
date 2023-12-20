row = int(input("Enter row: "))
col = int(input("Enter col: "))

print("Enter matrix1: ")
matrix1 = [[int(input()) for i in range(row)] for j in range(col)]

print("Enter matrix2: ")
matrix2 = [[int(input()) for i in range(row)] for j in range(col)]

sum_matrix = [[0 for i in range(row)] for j in range(col)]

for i in range(row):
    for j in range(col):
        for k in range(row):
            sum_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for i in range(row):
    for j in range(col):
        print(sum_matrix[i][j], end=" ")
    print()