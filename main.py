from Matrix import Matrix, Vector

try:
    data1 = [[1, 2], [6, 1], [8, 2], [9, 3]]
    A = Matrix(data1)

    data2 = [[3, 4, 3], [5, 8, 7]]
    B = Matrix(data2)

    data3 = [1, 2, 3]
    a = Vector(data3)

    data4 = [8, 1]
    b = Vector(data4)



    print(A*a)
except Exception as e:
    print(e)