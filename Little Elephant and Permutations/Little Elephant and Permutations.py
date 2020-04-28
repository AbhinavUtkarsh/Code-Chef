#https://www.codechef.com/problems/LEPERMUT
for i in range(int(input())):
    N=int(input())
    Listy=list(map(int,input().split()))
    if len(Listy)==1:
        print("YES")
    else:
        inversion_counter=0
        for i in range(N):
            for j in range(i+1,N):
                if Listy[i]>Listy[j]:
                    inversion_counter=inversion_counter+1
        local_inversion_counter=0
        for i in range(N-1):
                if Listy[i]>Listy[i+1]:
                    local_inversion_counter=local_inversion_counter+1
        if local_inversion_counter==inversion_counter:
            print("YES")
        else:
            print("NO")
    