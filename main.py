from Matrix import Matrix, Vector

import time

try:
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]
    data2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    data3 = [[5, 2], [1, 7], [9, 1]]
    data4 = [[8, 1], [3, 1], [10, 2]]

    data5 = [9, 3, 8, 1]
    data6 = [8, 3, 2, 1]
    data7 = [3, 2]


    # Matrixer
    A = Matrix(data)
    B = Matrix(data2)
    C = Matrix(data3)
    D = Matrix(data4)

    # Vektorer
    a = Vector(data5)
    b = Vector(data6)
    c = Vector(data7)

    start = time.time()

    # Indsæt regnestykke på næste linje, prøv at gange nogle af dataerne sammen NOTER: Fejlkoder står på engelsk
    E = A*c
    # Kør programmet når du har lavet regnestykket

    end = time.time()
    tookTime = end - start
    print(f"{E}, took {tookTime} seconds")
except Exception as e:
    print(e)