from Matrix import Matrix, Vector

try:
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    data2 = [[1, 2], [3, 4], [5, 6]]
    data3 = [[5, 2], [1, 7], [9, 1]]
    data4 = [[8, 1], [3, 1], [10, 2]]

    data5 = [9, 3, 8, 1]
    data6 = [8, 3]
    data7 = []
    data8 = [[]]
    data9 = [[], []]

    A = Matrix(data)
    B = Matrix(data2)
    C = Matrix(data3)
    D = Matrix(data4)

    a = Vector(data5)
    b = Vector(data6)

    # c = Vector(data7)
    # E = Matrix(data8)
    # F = Matrix(data9)

    print(a)
except Exception as e:
    print(e)