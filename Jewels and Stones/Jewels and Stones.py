#https://www.codechef.com/problems/STONES
from collections import Counter

for i in range(int(input())):
    J=input() # aaa
    S=input() # a
    Count=0
    J_Count=Counter(J)
    S_Count=Counter(S)
    for i in J_Count.keys():
        for j in S_Count.keys():
            if i==j:
                Count=Count+S_Count[i]
                break
    print(Count)