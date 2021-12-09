from Matrix import Matrix
from Vector import Vector
import ext_class_func as ecf

try:
    data1 = [[1, 2], [6, 1], [8, 2], [9, 3]]
    a = Matrix(data1)

    data2 = [[3, 4], [5, 8]]
    b = Matrix(data2)

    data3 = [1, 2, 3]
    c = Vector(data3)



    print(Vector.scalar(c, c))
except Exception as e:
    print(e)