def gcd(a, b):
    small = min(a, b)
    big = max(a, b)
    while small:
        big, small = small, big % small
    return big


for _ in range(int(input())):
    n = int(input())
    sequence = list(map(int, input().split()))
    gcd_v = gcd(sequence[0], sequence[1])
    for i in range(1, n):
        gcd_v = gcd(gcd_v, sequence[i])
    print(gcd_v)
