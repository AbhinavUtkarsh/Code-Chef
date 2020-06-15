# https://www.codechef.com/JUNE20B/problems/CHFICRM

for _ in range(int(input())):
    n = int(input())
    coinValue = list(map(int, input().split()))
    balance = {5: 0, 10: 0, 15: 0}
    flag = True
    for i in range(n):
        if coinValue[i] == 15:
            if balance[5] <= 1 and balance[10] == 0:
                flag = False
                break
            else:
                balance[15] += 1
                if balance[10] != 0:
                    balance[10] -= 1
                else:
                    balance[5] -= 2

        elif coinValue[i] == 10:
            if balance[5] == 0:
                flag = False
                break
            else:
                balance[10] += 1
                balance[5] -= 1
        elif coinValue[i] == 5:
            balance[5] += 1
    if flag == True:
        print("YES")
    else:
        print("NO")
