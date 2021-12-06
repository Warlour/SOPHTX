class Matrix:
    def __init__(self, matrixList = [[]]):
        for row in matrixList:
            if (len(row) != len(matrixList[0])):
                raise ValueError("Length of row and column of matrix is not the same")
            

        self.data = matrixList
        self.size = [len(matrixList), len(matrixList[0])]
    
if (__name__ == "__main__"):
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    m = Matrix(data)
    print(m.size)

    data2 = [[1, 2], [3, 4], [5, 6], [2, 4]]
    a = Matrix(data2)
    print(a.size)