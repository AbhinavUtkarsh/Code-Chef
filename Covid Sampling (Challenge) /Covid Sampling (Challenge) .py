# https://www.codechef.com/JUNE20B/problems/COVDSMPL
import sys

for _ in range(int(input())):
    n, p = map(int, input().split())
    solution = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(0, n):
            query = [1, i + 1, j + 1, i + 1, j + 1]
            print(*query)
            sys.stdout.flush()
            grader = int(input())
            if grader == 1:
                solution[i][j] = 1
            elif grader == -1:
                exit()
    print(2)
    sys.stdout.flush()
    for i in range(n):
        for j in range(n):
            print(solution[i][j], end=" ")
        print()
    sys.stdout.flush()
    grader = int(input())
    if grader == -1:
        exit()
