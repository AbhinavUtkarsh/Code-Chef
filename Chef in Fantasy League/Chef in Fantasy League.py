

for i in range(int(input())):
    N,S=map(int,input().split())
    Price = list(map(int, input().split()))
    Marker = list(map(int, input().split()))
    
    
    Forward_min=999
    Defender_min=999
    for i in range(N):
        if Marker[i]==0:
            if Defender_min>Price[i]:
                Defender_min=Price[i]
        else:
            if Forward_min>Price[i]:
                Forward_min=Price[i]
    Cost=Forward_min+Defender_min
    Balance=100-S
    if Cost<=Balance:
        print("yes")
    else:
        print("no")