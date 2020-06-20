# https://www.codechef.com/problems/ALEXNUMB
for _ in range(int(input())):
    n = int(input())
    listy = list(map(int, input().split()))
    count = 0
    print(int(n * ((n - 1) / 2)))

