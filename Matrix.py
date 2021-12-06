class Matrix:
    def __init__(self, a = [[]]):
        self.a = a
        for row in a:
            if (len(row) != len(a[0])):
                raise ValueError("Length of row and column of matrix is not the same")
            

        self.data = a
        self.size = [len(a), len(a[0])]

    # def __add__(self, b = [[]]):
    #     self.b = b
    #     for row in b:
    #         if (len(row) != len(b[0])):
    #             raise ValueError("Length of row and column of second matrix is not the same")

    #     for row in b:
    #         # raise if row and column in a and b not the same

    #     a_row = len(self.a)
    #     a_col = len(self.a[0])

    #     b_row = len(self.b)
    #     b_col = len(self.b[0])

    #     sum = []

    #     for r in range(a_row):
    #         for c in range(a_col):
    #             for r2 in range(b_row):
    #                 for c2 in range(b_col):
    #                     sum.append([])


    
if (__name__ == "__main__"):
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    a = Matrix(data)
    print(a.size)

    data2 = [[1, 2], [3, 4], [5, 6], [2, 4]]
    b = Matrix(data2)
    print(b.size)

    #print(a + b)