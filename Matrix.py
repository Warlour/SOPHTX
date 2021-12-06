class Matrix:
    def __init__(self, a = [[]]):
        self.a = a
        for row in self.a:
            if (len(row) != len(self.a[0])):
                raise ValueError("Length of row and column of matrix is not the same")
            

        self.data = a
        self.size = [len(self.a), len(self.a[0])]

    def __add__(self, other):

    #    for row in b:
    #        if (len(row) != len(b[0])):
    #            raise ValueError("Length of row and column of second matrix is not the same")

    #    for row in b:
    #         raise if row and column in a and b not the same

        a_row = len(self.a)
        a_col = len(self.a[0])

        sum = []
        
        '''
        List in list is added with zero values, in order to change later on
        Based on the first row of 'a'
        '''
        for r in range(a_row):
            sum.append([])
            for c in range(a_col):
                sum[r].append(0)

        for r in range(a_row):
            for c in range(a_col):
                sum[r][c] = self.a[r][c] + other.a[r][c]
        return sum


    
if (__name__ == "__main__"):
    # size = [row, col]

    # size = [2, 4]
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    a = Matrix(data)

    # size = [2, 4]
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    b = Matrix(data2)

    # size = [2, 4]
    data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    c = Matrix(data3)

    print(a + b)

    # ab = a + b
    # print(ab + c)
    # TypeError: can only concatenate list (not "Matrix") to list

    # Følgende virker, dvs. at returningsværdien for __add__ skal være en matrix fra Matrix-klassen
    ab = Matrix(a + b)
    print(ab + c)

    # print(a + b + c)
    # TypeError: can only concatenate list (not "Matrix") to list