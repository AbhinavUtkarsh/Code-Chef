#https://www.codechef.com/MAY20B/problems/SORTVS
import collections

def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    num=root
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited and neighbour!=num: 
                visited.add(neighbour) 
                queue.append(neighbour)
    return list(visited)

def get_non_sorted_min(array,num):
    for i in range(len(array)):
        if i+1!=array[i] and array[array.index(i+1)]>num:
            return array.index(i+1)
    return -1

for _ in range(int(input())):
    n,m=map(int,input().split())
    array=list(map(int,input().split()))
    robot=[]
    for i in range(m):
        swap=[]
        swap=list(map(int,input().split()))
        robot.append(swap)
    counter=0
    connections=[ [ 0 for i in range(n) ] for j in range(n) ] 
    for i in range(n):
        for j in range(n):
            for k in range(len(robot)):
                for l in range(0,1):
                    connections[robot[k][l]-1][robot[k][l+1]-1]=1
                    connections[robot[k][l+1]-1][robot[k][l]-1]=1
    connections=matrix_to_list(connections)
    print(connections)
    j=array.index(min(array))
    print("J initially",j)
    while(j<n):
        copy=array[j]
        print("COPY",copy,"J CURRENTLY",j,"ARRAY CURRENTLY",array)
        if j==-1:
            break
        if j+1!=array[j]:
            powers=bfs(connections,j)
            print("POWER OF",j,"is",powers)
            for i in range(len(powers)):
                k=0
                if (copy-1) in powers and j+1!=array[j] and (powers[k]+1 !=array[powers[k]]):
                    temp1=array[copy-1]
                    array[copy-1]=array[j]
                    array[j]=temp1
                    print("swapping",array[copy-1],array[j])
                    print("AFTER SWAP DIRECT",array)
                    k+=1
                elif (powers[i]+1 !=array[powers[i]] ) and j+1!=array[j]:
                    temp=array[powers[i]]
                    array[powers[i]]=array[j]
                    array[j]=temp
                    print("swapping",array[powers[i]],array[j])
                    print("AFTER SWAP INDIRECT",array)
        print(array)
        j=get_non_sorted_min(array,copy)
    j=0
    while(j<n):
        if j+1!=array[j]:
            #print("HUMAN",array[j],array[array[j]-1])
            temp3=array[j]
            array[j]=array[array[j]-1]
            array[temp3-1]=temp3
            counter+=1
        else:
            j+=1
    print(counter)