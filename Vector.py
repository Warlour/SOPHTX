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
        return str("You cannot multiply two vectors. However, you can calculate the scalarproduct using Vector.scalar(vector, vector)")
    
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
        return str(self.data)

if (__name__ == "__main__"):
    data = [5, 2, 2]
    a = Vector(data)

    data2 = [3, 7, 9]
    b = Vector(data2)

    print(Vector.scalar(a, b))