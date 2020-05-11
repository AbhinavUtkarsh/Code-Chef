#https://www.codechef.com/MAY20B/problems/NRWP
for _ in range(int(input())):
    h,w,n=map(int,input().split())
    matrix=[]
    for i in range(h):
            matrix.append(list(map(int,input().split())))
    values=[]
    for i in range(n):
            values.append(list(map(int,input().split())))
    
    particles=[[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(len(values)):
                particles[values[k][0]-1][values[k][1]-1]=values[k][2]
    # till here only input has been taken and kept into 2 matrices
    
    maxima=-9999999999
    V=0
    for k in range(h*w+1):
        for i in range(h):
            for j in range(w):
                if k==0:
                    particles[0][0]=-1*particles[0][0]
                elif k==1:
                    particles[0][1]=-1*particles[0][1]
                elif k==2:
                    particles[1][0]=-1*particles[1][0]
                elif k==4:
                    particles[1][1]=-1*particles[1][1]
                V+=matrix[i][j]*particles[i][j]
                if V>maxima:
                    maxima=V
    print(particles)
    print(matrix)
    print(V)