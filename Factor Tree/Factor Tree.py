#https://www.codechef.com/APRIL20B/problems/FCTRE
import numpy as np 

Test=int(input())

def number_of_factors(number):
    
    
    pass
    return 0

def DFS(visited,from_vertex,to_vertex,Stack):
    
    Stack.append(from_vertex)
    if(from_vertex==to_vertex):
        Path.append(from_vertex)
        return Path
    visited[from_vertex]=True
    flag=0
    
    if(len(Adj_List[from_vertex])>0):
        
        for j in Adj_List[from_vertex]:
            if(visited[j]==False):
                DFS(visited,j,to_vertex,Stack)
                print(flag)
                flag=1
            
    print("Stack: ",Stack)
    print("Flag: ",flag) 
    print("Visited: ",visited) 
    if flag==0:
        print("Stack[-1]",Stack[-1])
        del Stack[-1]
        

    return Stack

def DFS_calling(from_vertex,to_vertex,N,Stack,Adj_List,Q):
    visited = [0 for i in range(N+1)]
    print("Visited",visited)
    return (DFS(visited,from_vertex,to_vertex,Stack))
    
    
while(Test!=0):
    
    #Input Start
    N=int(input())
    False_A_Matrix=np.zeros((N-1,2))
    for i in range(N-1):
        False_A_Matrix[i]=input().split(" ")
    Costs = list(map(int, input().split()))
    Q=int(input())
    Queries=np.zeros((Q,2))
    for i in range(Q):
        Queries[i]=input().split(" ")
    #Input End
    
    rows=[]
    for i in range(0,N-1):
        rows.append(int(False_A_Matrix[i][0]))  
        
    Adj_List={listy: [] for listy in range(1,N+1)}
    counter=0
    for i in rows:
        Adj_List[i].append(int(False_A_Matrix[counter][1]))
        Adj_List[int(False_A_Matrix[counter][1])].append(i)
        counter=counter+1
        
        
    Nav=[]
    for i in range(0,Q):
        Stack=[]
        Path=[]
        Nav.append(DFS_calling(int(Queries[i][0]),int(Queries[i][1]),N+1,Stack,Adj_List,Q))
    
    Total_cost=[]
    
    for i in range(0,len(Nav)):
        Sum=0
        for j in range(0,len(Nav[i])):
            Sum=Sum+Costs[Nav[i][j]-1]
            print("Costs", Nav[i][j]-1,Costs[Nav[i][j]-1])
    
        Total_cost.append(Sum)
    
    print(Nav)
    print(Adj_List)
    print(Total_cost)
    
    Test=Test-1