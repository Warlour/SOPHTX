a = [[1, 2, 3], [4, 5, 6], [2, 2]]

a_row = len(a)
a_col = len(a[0])

sum = []

for r in range(a_row):
    sum.append([])
    for c in range(a_col):
        sum[r].append(0)

print(sum)
