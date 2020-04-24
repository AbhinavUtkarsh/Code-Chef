#https://www.codechef.com/LRNDSA01/problems/CARVANS

for _ in range(int(input())):
    Number_of_Cars=int(input())
    Max_Speed=list(map(int,input().split()))
    Index_Marker=0
    Min=0
    Counter=1
    for i in range(Number_of_Cars):
        Index_Marker=Max_Speed[i]
        if i==0:
            Min=Index_Marker
        elif( Index_Marker <= Min):
            Min=Index_Marker
            Counter=Counter+1
    print(Counter)