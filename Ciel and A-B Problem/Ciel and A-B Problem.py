#https://www.codechef.com/problems/CIELAB

A,B=map(int,input().split())

Sub=A-B
Number=10**(len(str(Sub))-1)
if int(str(Sub)[0])==9:
    Sub=Sub-Number
else:
    Sub=Sub+Number
print(Sub)