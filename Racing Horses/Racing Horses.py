#https://www.codechef.com/problems/HORSES
for i in range(int(input())):
    Number_of_Horses=int(input())
    Skills=list(map(int,input().split()))
    Skills.sort()
    Diff=[]
    for i in range(Number_of_Horses-1):
        Diff.append(Skills[i+1]-Skills[i])
    print(min(Diff))