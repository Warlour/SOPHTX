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