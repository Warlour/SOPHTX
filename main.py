from Matrix import Matrix, Vector

import time

try:
    data1 = [[76, 23, 95], [12, 87, 43], [76, 15, 98]]
    data2 = [[87, 34, 76], [23, 43, 12], [98, 23, 54]]

    A = Matrix(data1)
    B = Matrix(data2)

    data3 = [[75, 22, 59], [12, 86, 45]]
    data4 = [[76, 54], [12, 98], [34, 56]]

    D = Matrix(data3)
    E = Matrix(data4)

    F = D*E

    data5 = [[76, 32, 98, 87], [54, 87, 12, 43]]
    data6 = [63, 37, 72, 18]

    G = Matrix(data5)
    a = Vector(data6)

    start = time.time()

    # Indsæt regnestykke på næste linje, prøv at gange nogle af dataerne sammen NOTER: Fejlkoder står på engelsk
    b = G*a
    # Kør programmet når du har lavet regnestykket

    b = G*a
    
    end = time.time()
    tookTime = end - start
    print(f"Produkt{b}")
except Exception as e:
    print(e)