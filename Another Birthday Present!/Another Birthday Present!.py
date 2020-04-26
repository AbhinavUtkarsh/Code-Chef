for i in range(int(input())):
    N,K=map(int,input().split())
    Presents = list(map(int, input().split()))
    Copy=sorted(Presents)
    if K==1:
        print("yes")
        continue
    for i in range(N):
        flag=0
        for j in range(i%K,N,K):
            if Copy[i]==Presents[j]:
                flag=1
                break
        else:
            print("no")
            break
    else:
        print("yes")