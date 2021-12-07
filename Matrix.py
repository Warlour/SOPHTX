class Matrix:
    def __init__(self, a = [[]]):
        for row in a:
            if(len(row) != len(a[0])):
                raise ValueError("Length of row and column of matrix is not the same")
        
        self.size = [len(a), len(a[0])]

        self.data = a
        

    def __add__(self, other):
        if(type(other) != type(Matrix())):
            raise TypeError("Second argument is not a matrix")

        # raise ValueError if first and second matrix not equal in size
        if(self.size != other.size):
            raise ValueError("Dimensions of Matrix does not match")

        a_row = len(self.data)
        a_col = len(self.data[0])

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
                sum[r][c] = self.data[r][c] + other.data[r][c]
        return Matrix(sum)

    def __multiply__(self, other):
        pass

    def __str__(self):
        return str(self.data)



    
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

    data4 = [[1, 2], [3, 4], [5, 6]]
    d = Matrix(data4)
    
    print(a)
    print(b)
    print(c)

    print(a + b + c)