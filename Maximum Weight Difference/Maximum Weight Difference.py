#https://www.codechef.com/problems/MAXDIFF

for i in range(int(input())):
    N,K=map(int,input().split())
    weight=list(map(int,input().split()))
    weight.sort()
    if K>N//2:
        K=N-K
    total_sum=sum(weight)
    sum_of_K_items=sum(weight[:K])
    sum_of_other_set=total_sum-sum_of_K_items
    diff=abs( sum_of_other_set-sum_of_K_items)
    print(diff)
