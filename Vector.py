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

        for i in self.data:
            print()

        #return Vector(sum)

    def __str__(self):
        return str(self.data)

if (__name__ == "__main__"):
    data2 = [5, 2, 2]
    b = Vector(data2)

    print(b)
    print(b.size)
    print(b+b)