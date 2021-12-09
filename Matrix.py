from Vector import Vector

class Matrix:
    def __init__(self, a = [[]]):
        for row in a:
            if(len(row) != len(a[0])):
                raise ValueError(f"A matrix must have the same amount of values in each row and column.\nYours did not: {a}")

        self.size = [len(a), len(a[0])]
        self.data = a

    # Addition of two matrixes
    def __add__(self, other):
        if(type(other) != type(Matrix())):
            raise TypeError(f"{other} is not a matrix, specify with Matrix()")

        if(self.size != other.size):
            raise ValueError(f"Dimensions of either matrix does not match [rows, columns]\nSize of first matrix: {self.size}\nSize of second matrix: {other.size}")

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

    # Multiply two matrixes
    def __mul__(self, other):
        if (type(other) == type(Matrix())):
            pass
        elif (type(other) == type(Vector())):
            

    # 
    def __str__(self):
        return str(self.data)

if (__name__ == "__main__"):
    try:
        data = [[1, 2, 3, 4], [5, 6, 7, 8]]
        data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
        data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
        data4 = [[1, 2], [3, 4], [5, 6]]
        data5 = [[5, 2], [1, 7], [9, 1]]
        data6 = [[8, 1], [3, 1], [10, 2]]

        a = Matrix(data)
        b = Matrix(data2)
        c = Matrix(data3)
        d = Matrix(data4)
        e = Matrix(data5)
        f = Matrix(data6)
        print(f"a + b + c = {a + b + c}\n")
        print(f"d + e + c = {d + e + f}")
    except Exception as e:
        print(e)