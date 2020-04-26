# #https://www.codechef.com/LRNDSA01/problems/CONFLIP
for i in range(int(input())):
    for j in range(int(input())):
        I,N,Q=map(int,input().split())
        if N%2==0:
            print(N//2)
        else:
            Counting=[0,0,0]
            if I==1:
                Counting[1]=N//2
                Counting[2]=N//2 + 1
            else:
                Counting[2]=N//2
                Counting[1]=N//2 + 1
            print(Counting[Q])
