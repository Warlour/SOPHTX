m = [[1, 2, 3], [4, 5, 6]]
v = [7, 8, 9]

def mvP(matrix, vector):
    '''Returns a vector\n\nParameters: matrix, vector'''
    
    row = len(matrix)
    col = len(matrix[0])
    mvP = []

    for _ in range(row):
        mvP.append(0)

    for i in range(row):
        for j in range(col):
            mvP[i] = (mvP[i] + matrix[i][j] * vector[j])
    return mvP

print(mvP(m, v))