x = [[1,5,4],[2,3,6],[4,8,9]]
y = [[2,9,3],[4,8,1],[5,7,6]]

r = []

for i in range(len(x)):
    n = []
    for j in range(len(x)):
        z = 0
        for k in range(len(x)):
            xx = x[k]
            yy = y[j]
            z += xx[j] * yy[k]
        n.append(z)
    r.append(n)

print r
