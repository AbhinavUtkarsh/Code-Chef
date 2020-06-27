# https://www.codechef.com/LTIME85B/problems/CHFMOT18
for _ in range(int(input())):
    s, n = map(int, input().strip().split())
    counter = 0
    counter = s // n
    rem = s % n
    if s < n:
        if rem % 2 == 0 or rem == 1:
            print(1)
        else:
            print(2)
    elif s == n:
        print(1)
    else:
        if rem == 0:
            pass
        elif rem % 2 == 0 or rem == 1:
            counter += 1
        else:
            counter += 2
        print(counter)
