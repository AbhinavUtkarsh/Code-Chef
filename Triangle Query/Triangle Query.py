def are(x,y,z):
    return abs(((x[0]*(y[1]-z[1])))+((y[0]*(z[1]-x[1])))+((z[0]*(x[1]-y[1]))))/2

for i in range(int(input())):
    N,Q=map(int,input().split())
    N_Cord=[]
    for i in range(N):
        N_Cord.append(list(map(int,input().split())))
    Triangle_Cord=[]
    for i in range(Q):
        Triangle_Cord.append(list(map(int,input().split())))
    Counter=0
    for i in range(0,Q):
        Counter=0
        A=[Triangle_Cord[i][0],0]
        B=[Triangle_Cord[i][1],0]
        C=[Triangle_Cord[i][0]+abs(Triangle_Cord[i][1]-Triangle_Cord[i][0])/2,abs(Triangle_Cord[i][1]-Triangle_Cord[i][0])/2]
        Area=(0.5*abs((B[0]-A[0]))*((B[0]-A[0])/2))
        for j in range(0,N):
            Area_OAB=0
            Area_OBC=0
            Area_OCA=0
            Area_OAB=are(A,B,N_Cord[j])
            Area_OBC=are(B,C,N_Cord[j])
            Area_OCA=are(C,A,N_Cord[j])
            if Area==Area_OAB+Area_OBC+Area_OCA:
                Counter=Counter+1
        print(Counter,end=" ")
        
    