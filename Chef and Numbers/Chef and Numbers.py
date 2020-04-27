#https://www.codechef.com/problems/RECNDNOS
from collections import Counter
import operator
for i in range(int(input())):
    n=int(input())
    dishes=list(map(int,input().split()))
    setarray=[]
    dummy=[]
    for i in dishes:
        if i not in setarray:
            setarray.append(i)
    setarray.sort()
    for i in setarray:
        indices=[]
        for j in range(n):
            if dishes[j]==i:
                if j-1 not in indices:
                    indices.append(j)
        dummy.append(len(indices))
    print(setarray[dummy.index(max(dummy))])