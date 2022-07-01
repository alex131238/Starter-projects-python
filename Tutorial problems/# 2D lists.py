# 2D lists

# yay lots of indexing

Matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Matrix_1[0][0] = 20
print(Matrix_1[0][0])

for row in Matrix_1:
    for item in row:
        print(item)

