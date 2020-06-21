# https://www.codechef.com/COOK119B/problems/CACHEHIT
import math

for _ in range(int(input())):
    array_size, block_size, m = map(int, input().split())
    access = list(map(int, input().split()))
    counter = 0
    loaded = -1
    for i in range(m):
        if loaded != math.ceil(access[i] // block_size):
            loaded = math.ceil(access[i] // block_size)
            counter += 1
    print(counter)

