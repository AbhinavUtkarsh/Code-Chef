#https://www.codechef.com/COOK117B/problems/LIFTME
import numpy as np
test=int(input())
while(test!=0):
    
    N,Q=map(int,input().split())
    distance_counter=0
    floors=[ [ 0 for i in range(2) ] for j in range(Q) ] 
    for i in range(0,Q):
        for j in range(0,1):
            floors[i][j],floors[i][j+1]=map(int,input().split())
    distance_counter=floors[0][0]
    for i in range(0,Q):
        for j in range(0,1):
            if i==Q-1:
                distance_counter=distance_counter+abs(floors[i][j]-floors[i][j+1])
            else:
                distance_counter=distance_counter+abs(floors[i][j]-floors[i][j+1])+abs(floors[i][j+1]-floors[i+1][j])
    print(distance_counter)
    test=test-1