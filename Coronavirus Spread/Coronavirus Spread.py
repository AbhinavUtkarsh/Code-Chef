#https://www.codechef.com/MAY20B/problems/COVID19

for _ in range(int(input())):
    n=int(input())
    dist=list(map(int,input().split()))
    diff=[]
    minima=9999999
    maxima=-9999999
    current=1
    for i in range(1,n):
        if dist[i]-dist[i-1]>2:
            minima=min(minima,current)
        if dist[i]-dist[i-1]>2:
            maxima=max(maxima,current)
        if dist[i]-dist[i-1]<3:
            current=current+1
        else:
            current=1
    minima=min(minima,current)
    maxima=max(maxima,current)
    print(minima,maxima)