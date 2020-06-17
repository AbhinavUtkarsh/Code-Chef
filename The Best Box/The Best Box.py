for _ in range(int(input())):
    p, s = map(int, input().strip().split())
    a = (p - pow((((p ** 2) - (24 * s))), 0.5)) / 12
    v = (a * s) / 2 - ((a ** 2) * p / 4) + a ** 3
    print(round(v, 2))
