# https://www.codechef.com/LTIME85B/problems/INCRDEC
for _ in range(int(input())):
    n = int(input())
    seq = list(map(int, input().strip().split()))
    if len(seq) == len(set(seq)):
        print("YES")
        print(*sorted(seq))
    else:
        hashtable = {}
        for i in range(len(seq)):
            if seq[i] not in hashtable:
                hashtable[seq[i]] = 1
            else:
                hashtable[seq[i]] += 1
        maxima = max(seq)
        flag = 0
        for i in hashtable:
            if hashtable[i] > 2 or hashtable[maxima] > 1:
                print("NO")
                flag = 1
                break
        if flag == 0:
            dummy = [0] * 1000001  #
            res = []
            for i in seq:
                dummy[i] += 1
            # print(dummy)
            for i in range(maxima + 1):
                if dummy[i] != 0:
                    res.append(i)
                    dummy[i] -= 1
            # print(dummy)
            for i in range(maxima, -1, -1):
                if dummy[i] != 0:
                    res.append(i)
                    dummy[i] -= 1
            print("YES")
            print(*res)
