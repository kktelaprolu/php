def add_matrix(M1,M2):
    for i in range(0,len(M1)):
        for j in range(0,len(M2)):
            M3[i][j] = M1[i][j] + M2[i][j]
    return(M3)

M1 = [[5,7,9],
     [8,12,4],
     [0,6,3]]
M2 = [[3,3,3],
     [5,5,5],
     [8,8,8]]
M3= [[0,0,0],[0,0,0],[0,0,0]]
Final_matrix= add_matrix(M1,M2)
for k in Final_matrix:
    print (k)

