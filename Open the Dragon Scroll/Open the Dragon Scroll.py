for _ in range(int(input())):
    n, a, b = map(int, input().split())
    a = bin(a)[2:]
    a = a[::-1]
    while len(a) != n:
        a = a + "0"
    a = a[::-1]
    b = bin(b)[2:]
    b = b[::-1]
    while len(b) != n:
        b = b + "0"
    b = b[::-1]
