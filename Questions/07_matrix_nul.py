row = int(input("Enter row: "))
col = int(input("Enter col: "))

print("Enter matrix1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]

print("Enter matrix2: ")
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]

product_matrix = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        for k in range(row):
            product_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print("Product Matrices: ")

for i in range(row):
    for j in range(col):
        print(product_matrix[i][j], end=" ")
    print()