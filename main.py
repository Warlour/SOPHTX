from Matrix import Matrix
from Vector import Vector
import ext_class_func as ecf

data1 = [[1, 2], [6, 1], [8, 2], [9, 3]]
a = Matrix(data1)

data2 = [3, 4]
b = Vector(data2)

print(ecf.mvP(a, b))