for i in range(int(input())):
    N=int(input())
    Song_Length=list(map(int,input().split()))
    K=int(input())
    Our_Song=Song_Length[K-1]
    Counter=1
    for i in Song_Length:
        if i<Our_Song:
            Counter=Counter+1
    print(Counter)