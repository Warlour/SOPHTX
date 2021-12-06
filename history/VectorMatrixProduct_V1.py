m = [[1, 2, 3], [4, 5, 6]]
v = [7, 8, 9]

def mvP(matrix, vector):
    # Vector length must match number of matrix columns; vectorLen = 2, matrix = [[x0, y0], [x1, y1]]
    # We can take the length of the matrix's first list as a length of columns, however, this does not account for missing values if next row in the last column is missing
    row = len(matrix)
    col = len(matrix[0])
    
    mvP = [0, 0]

    for i in range(row):
        for j in range(col):
            mvP[i] = (mvP[i] + m[i][j] * v[j])
    return mvP

print(mvP(m, v))