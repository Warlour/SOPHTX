from Matrix import Matrix
from Vector import Vector

def mvP(matrix, vector):
    '''Returns a vector\n\nParameters: matrix, vector'''

    if(type(matrix) != type(Matrix())):
        raise TypeError("First argument should be of type Matrix")
    if(type(vector) != type(Vector())):
        raise TypeError("Second argument should be of type Vector")
    row = len(matrix)
    col = len(matrix[0])
    mvP = []

    for _ in range(row):
        mvP.append(0)

    for i in range(row):
        for j in range(col):
            mvP[i] = (mvP[i] + matrix[i][j] * vector[j])
    return mvP
