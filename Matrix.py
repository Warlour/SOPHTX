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

    # Multiply
    def __mul__(self, other):
        # Multiply two matrixes
        if (type(other) == type(Matrix())):
            pass

        # Multiply matrix with vector
        elif (type(other) == type(Vector())):
            if (self.size[1] != other.size):
                raise ValueError("The length of the vector must be equal to the amount of columns in the matrix")
            
            prod = []

            for i in range(self.size[0]):
                prod.append(0)
                for j in range(self.size[1]):
                    prod[i] = (prod[i] + self.data[i][j] * other.data[j])
            return prod

        else:
            raise TypeError(f"{other} is an unknown datatype")
            

    def __str__(self):
        return str(self.data)

class Vector:
    def __init__(self, a = []):
        self.size = len(a)
        self.data = a

    def __add__(self, other):
        if (type(other) != type(Vector())):
            raise TypeError(f"{other} is not a vector")

        if (self.size != other.size):
            raise ValueError("Vectors are not of same length")

        sum = []
        for _ in self.data:
            sum.append(0)

        for i in range(len(sum)):
            sum[i] = self.data[i] + other.data[i]

        return Vector(sum)

    def __mul__(self, other):
        if (type(other) == type(Vector())):
            raise TypeError("You cannot multiply two vectors.\nHowever, you can calculate the scalarproduct using vector1.scalar(vector2)")
        elif (type(other) == type(Matrix())):
            raise TypeError("Vector-matrixproduct is not supported")
        else:
            raise TypeError(f"{other} is an unknown datatype")


    def scalar(self, other):
        '''Returns a constant\n\nParameters: vector, vector'''
        if (type(other) != type(Vector())):
            raise TypeError(f"{other} is not of type Vector")

        if (self.size != other.size):
            raise ValueError("Vectors must be same size")

        # Linear kombination
        lk = 0

        for i in range(len(self.data)):
            lk += self.data[i] * other.data[i]

        return lk

    def __str__(self):
        return "Vector column: " + str(self.data)

if (__name__ == "__main__"):
    try:
        data = [[1, 2, 3, 4], [5, 6, 7, 8]]
        data2 = [[1, 2], [3, 4], [5, 6]]
        data3 = [[5, 2], [1, 7], [9, 1]]
        data4 = [[8, 1], [3, 1], [10, 2]]
        data5 = [9, 3, 8, 1]
        data6 = [8, 3]

        A = Matrix(data)
        B = Matrix(data2)
        C = Matrix(data3)
        D = Matrix(data4)
        a = Vector(data5)
        b = Vector(data6)


        print(B*b)
    except Exception as e:
        print(e)