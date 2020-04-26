#https://www.codechef.com/problems/JOHNY
for i in range(int(input())):
    N=int(input())
    Song_Length=list(map(int,input().split()))
    K=int(input())
    Song_Length[K-1]=float(Song_Length[K-1])
    Song_Length.sort()
    for i in range(N):
        if type(Song_Length[i])==float:
            print(i+1)
