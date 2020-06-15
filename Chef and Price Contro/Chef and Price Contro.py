# https://www.codechef.com/JUNE20B/problems/PRICECON

for _ in range(int(input())):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    loss = 0
    for i in prices:
        if i > k:
            loss = loss + (i - k)
    print(loss)
