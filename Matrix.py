class Matrix:
    def __init__(self, a = [[]]):
        for row in a:
            if(len(row) != len(a[0])):
                raise ValueError("Length of row and column of matrix is not the same")
        
        self.size = [len(a), len(a[0])]

        self.data = a

    # Addition of two matrixes
    def __add__(self, other):
        if(type(other) != type(Matrix())):
            raise TypeError("Second argument is not a matrix")

        if(self.size != other.size):
            raise ValueError("Dimensions of Matrix does not match")

        a_row = len(self.data)
        a_col = len(self.data[0])

        sum = []

        for r in range(a_row):
            sum.append([])
            for c in range(a_col):
                sum[r].append(0)

        for r in range(a_row):
            for c in range(a_col):
                sum[r][c] = self.data[r][c] + other.data[r][c]
        return Matrix(sum)

    def __multiply__(self, other):
        pass

    def __str__(self):
        return str(self.data)

if (__name__ == "__main__"):
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    data4 = [[1, 2], [3, 4], [5, 6]]
    data5 = [[5, 2], [1, 7], [9, 1]]
    data6 = [[8, 1], [3, 1], [10, 9]]

    a = Matrix(data)
    b = Matrix(data2)
    c = Matrix(data3)

    print(a + b + c)

    d = Matrix(data4)
    e = Matrix(data5)
    f = Matrix(data6)

    print(d + e + f)