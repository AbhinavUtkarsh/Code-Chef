# https://www.codechef.com/JUNE20B/problems/XYSTR

for _ in range(int(input())):
    string = input()
    n = len(string)
    maxima = 0
    i = 0
    while i <= n - 2:
        if string[i] != string[i + 1]:
            maxima += 1
            i += 2
        else:
            i += 1
    print(maxima)
