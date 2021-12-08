from Vector import Vector
from Matrix import Matrix

def mvP(matrix, vector):
    '''Returns a vector\n\nParameters: matrix, vector'''
    if (type(matrix) != type(Matrix())):
        raise TypeError(f"{matrix} is not of type Matrix")
    if (type(vector) != type(Vector())):
        raise TypeError(f"{vector} is not of type Vector")

    if (matrix.size[1] != vector.size):
        raise ValueError("The length of the vector must be equal to the matrix's amount of columns")

    prod = []

    for i in range(matrix.size[0]):
        prod.append(0)
        for j in range(matrix.size[1]):
            prod[i] = (prod[i] + matrix.data[i][j] * vector.data[j])
    return prod


if (__name__ == "__main__"):
    data1 = [[1, 2, 3, 4], [8, 2, 1, 4]]
    m = Matrix(data1)

    data2 = [1, 5, 3, 5]
    v = Vector(data2)

    print(mvP(m, v))