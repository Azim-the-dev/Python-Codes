# Write a Program to calculate the sum and product of two compatible matrices. 

row = int(input("Enter number of rows: "))
col = int(input("Enter number of colums: "))

print("Enter matrix_1: ")
matrix_1 = [[int(input()) for i in range (col)] for j in range (row)]

print("Enter matrix_2: ")
matrix_2 = [[int(input()) for i in range (col)] for j in range (row)]

print("Sum Matrices: ")

sum_matrix = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        sum_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
        
for i in range(row):
    for j in range(col):
        print(sum_matrix[i][j],end=" ")
    print()