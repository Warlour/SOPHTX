from typing import Union

class Matrix:
    def __init__(self, a = [[]]):
        if ((type(a) and type(a[0])) != type(list())):
            raise TypeError(f"Matrix {a} is not of type matrix")

        # If matrix is empty | Didn't work
        # if (not a or not a[0]):
        #     raise ValueError(f"{a}: Matrix cannot be empty")

        for row in a:
            if (len(row) != len(a[0])):
                raise ValueError(f"A matrix must have the same amount of values in each row and column.\nYours did not: {a}")

        

        # [Rows, Columns]
        self.size = [len(a), len(a[0])]
        self.data = a

    # Addition
    def __add__(self, other: Union["Matrix", "Vector", "float"]):
        if (type(other) == type(Matrix())):
            if (self.size != other.size):
                raise ValueError(f"Dimensions of either matrix does not match [rows, columns]\nSize of first matrix: {self.size}\nSize of second matrix: {other.size}")

            sum = []
            for r in range(len(self.data)):
                sum.append([])
                for c in range(len(self.data[0])):
                    sum[r].append(0)
                    sum[r][c] = self.data[r][c] + other.data[r][c]
            return Matrix(sum)

        elif (type(other) == type(Vector())):
            if (self.size[0] != other.size):
                raise ValueError(f"The length of the vector must be equal to the amount of columns in the matrix")
            
            sum = self.data
            for r in range(self.size[0]):
                for c in range(self.size[1]):
                    sum[r][c] += other.data[r]
            return Matrix(sum)

        elif (type(other) == type(float)):
            sum = self.data
            for r in range(self.size[0]):
                for c in range(self.size[1]):
                    sum[r][c] += other
            return Matrix(sum)

        else:
            raise TypeError(f"{other} is an unknown datatype")

    # Multiply
    def __mul__(self, other: Union["Matrix", "Vector", "float"]):
        # Multiply two matrixes
        if (type(other) == type(Matrix())):
            # If height of self-matrix not equal to width of other-matrix
            if (self.size[1] != other.size[0]):
                raise ValueError(f"The amount of rows in the first matrix {self.size} must be equal to the amount of columns in the second matrix {other.size} ([Rows, Columns])")

            prod = []
            for i in range(self.size[0]):
                prod.append([])
                for j in range(other.size[1]):
                    prod[i].append(0)
                    for k in range(self.size[1]):
                        prod[i][j] += self.data[i][k]*other.data[k][j]
            return Matrix(prod)

        # Multiply matrix with vector
        elif (type(other) == type(Vector())):
            if (self.size[1] != other.size):
                raise ValueError("The length of the vector must be equal to the amount of columns in the matrix")
            
            prod = []
            for i in range(self.size[0]):
                prod.append(0)
                for j in range(self.size[1]):
                    prod[i] = (prod[i] + self.data[i][j] * other.data[j])
            return Vector(prod)

        elif (type(other) == type(float)):
            prod = self.data
            for r in range(self.size[0]):
                for c in range(self.size[1]):
                    prod[r][c] *= other
            return Matrix(prod)

        else:
            raise TypeError(f"{other} is an unknown datatype")

    def __str__(self):
        return str(self.data)

class Vector:
    def __init__(self, a = []):
        if (type(a) != type(list())):
            raise TypeError(f"Vector {a} is not of type vector")

        # If list is empty
        # if (not a):
        #     raise ValueError(f"{a}: Vector cannot be empty")

        self.size = len(a)
        self.data = a

    def __add__(self, other: Union["Matrix", "Vector", "float"]):
        if (type(other) == type(Vector())):
            if (self.size != other.size):
                raise ValueError("Vectors are not of the same length")

            sum = self.data
            for l in range(self.size):
                sum[l] += other.data[l]
            return Vector(sum)

        elif (type(other) == type(Matrix())):
            if (self.size != other.size[0]):
                raise ValueError(f"The vector length must be equal to the amount of rows in the matrix")

            sum = other.data
            for r in range(other.size[0]):
                for c in range(other.size[1]):
                    sum[r][c] += self.data[r]
            return Matrix(sum)

        elif (type(other) == type(float)):
            sum = self.data
            for l in range(self.size):
                sum[l] += other
            return Vector(sum)

        else:
            raise TypeError(f"{other} is an unknown datatype")

    def __mul__(self, other: Union["Matrix", "Vector", "float"]):
        if (type(other) == type(Vector())):
            raise TypeError("You cannot multiply two vectors.\nHowever, you can calculate the scalarproduct using vector1.scalar(vector2)")

        elif (type(other) == type(Matrix())):
            raise TypeError("Vector-matrixproduct is not supported")

        elif (type(other) == type(float)):
            prod = self.data
            for l in range(self.size):
                prod[l] *= other
            return Vector(prod)

        else:
            raise TypeError(f"{other} is an unknown datatype")


    def scalar(self, other: "Vector"):
        '''
        Returns a constant
        Parameters: vector, vector
        '''
        if (type(other) != type(Vector())):
            raise TypeError(f"{other} is not of type Vector")

        if (self.size != other.size):
            raise ValueError("Vectors must be same size")

        # Scalar product
        sclrprod = 0
        for i in range(len(self.data)):
            sclrprod += self.data[i] * other.data[i]
        return sclrprod

    def __str__(self):
        return str(self.data)

if (__name__ == "__main__"):
    data = [[1, 2.2, 3, 4], [5, 6, 7, 8]]
    data2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    data3 = [1, 5]
    data4 = [7, 2]
    data5 = [1, 2, 4, 9]

    A = Matrix(data)
    B = Matrix(data2)
    d = Vector(data3)
    e = Vector(data4)
    f = Vector(data5)

    print(A*f)