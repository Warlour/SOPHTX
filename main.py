from Matrix import Matrix, Vector

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

    print(a*b)
except Exception as e:
    print(e)