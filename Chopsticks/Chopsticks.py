#https://www.codechef.com/problems/TACHSTCK
N,D=map(int,input().split())
length=[]
for i in range(N):
    length.append(int(input()))

length.sort()
counter=0
i=0
while(i<N):
    if(i<N-1):
        if length[i+1]-length[i]<=D:
            counter+=1
            i+=2
        else:
            i+=1
    else:
        i+=1
print(counter)

