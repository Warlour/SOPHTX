class Vector:
    def __init__(self, a = []):
        self.size = len(a)
        self.data = a

    def __add__(self, other):
        if (self.size != other.size):
            raise ValueError("Vectors are not of same length")

        sum = []
        for _ in self.data:
            sum.append(0)

        for i in range(len(sum)):
            sum[i] = self.data[i] + other.data[i]

        return Vector(sum)

    def __mul__(self, other):
        return "You cannot multiply two vectors. However, you can calculate the scalarproduct using scalar(vector * vector)"
    
    def scalar(self, other):
        pass

    def __str__(self):
        return str(self.data)

if (__name__ == "__main__"):
    data2 = [5, 2, 2]
    b = Vector(data2)

    #print(b)
    #print(b.size)
    print(b*b)