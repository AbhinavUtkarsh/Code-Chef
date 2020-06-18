for _ in range(int(input())):
    m, w = map(str, input().split())
    short = ""
    long = ""
    if len(m) > len(w):
        short = w
        long = m
    else:
        short = m
        long = w
    flag = 0
    j = 0
    for i in range(len(short)):
        while j < len(long):
            if long[j] == short[i]:
                break
            j += 1
        if j > len(long):
            flag = 1
            print("NO")
            break
        j += 1
    if flag == 0:
        print("YES")

