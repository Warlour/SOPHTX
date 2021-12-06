m = []
mx = 1

while True:
    print(f"Indsæt første kolonne ... FIKS{mx}. matrix-værdi, skriv 'q' for at stoppe: ", end = "")
    mxin = input()
    if (mxin != 'q'):
        mxin = float(mxin)
        print(end = "\n")
        m.append(mxin)
        print(f"Matrixen indtil videre: {m}", end = "\n")
        mx += 1
    if (mxin == "q"):
        break

v = []
vx = 1

print(end = "\n\n")

while True:
    print(f"Indsæt {vx}. vektor-værdi, skriv 'q' for at stoppe: ", end = "")
    vxin = input()
    if (vxin != 'q'):
        vxin = float(vxin)
        print(end = "\n")
        v.append(vxin)
        print(f"Vektoren indtil videre: {v}", end = "\n")
        vx += 1
    if (vxin == "q"):
        break

def mvP(matrix, vector):
    # Vector length must match number of matrix columns; vectorLen = 2, matrix = [[x0, y0], [x1, y1]]
    # We can take the length of the matrix's first list as a length of columns, however, this does not account for missing values if next row in the last column is missing
    row = len(matrix)
    col = len(matrix[0])
    
    mvP = []

    for _ in range(row):
        mvP.append(0)

    for i in range(row):
        for j in range(col):
            mvP[i] = (mvP[i] + m[i][j] * v[j])
    return mvP



print(f"Matrix vektor produktet er: {mvP(m, v)}")