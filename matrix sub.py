x=[[1,2,3,],[9,8,7,],[8,7,6]]
y=[[2,3,4],[5,6,7,],[8,5,3]]
z=[[0,0,0,],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        z[i][j]=x[i][j]-y[i][j]
for r in z:
    print(r)

