import math

for _ in range(int(input())):
    s, n = map(int, input().strip().split())
    print(math.ceil((s - (s % 2)) / n) + (s % 2))
