# https://www.codechef.com/COOK119B/problems/MAXMEX

for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    sequence = list(map(int, input().strip().split()))
    flag = 0
    temp = min(sequence)
    seq_set = set(sequence)
    for i in range(temp, m):
        if i not in seq_set:
            flag = 1
            break
    if flag == 1:
        print("-1")
    else:
        print(n - sequence.count(m))

