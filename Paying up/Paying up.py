#https://www.codechef.com/problems/MARCHA1
# for i in range(int(input())):
#     n,m=map(int,input().split())
#     notes=[0 for i in range(n)]
#     for i in range(n):
#         notes[i]=int(input())
#     notes.sort(reverse=True)
#     for i in range(n):
#         if m>=notes[i]:
#             m=m-notes[i]
#     if m==0:
#         print("Yes")
#     else:
#         print("No")

from itertools import combinations
for i in range(int(input())):
    n,m=map(int,input().split())
    notes=[0 for i in range(n)]
    for i in range(n):
        notes[i]=int(input())
    flag=0
    for i in range(n):
        for j in list(combinations(notes,i+1)):
            if sum(j)==m:
                flag=1
                break
    if flag==1:
        print("Yes")
    else:
        print("No")
            