#https://www.codechef.com/APRIL20B/problems/COVIDLQ#
Test=int(input())

def cal(Spots):
    flag1=0
    for i in range(0,len(Spots)):
        if Spots[i] == 1:
            
            for j in range(i+1,len(Spots)):
                if Spots[j]== 1 and j-i<6:
                    flag1=1
                    print("NO")
                    return
    if flag1==0:
        print("YES")
        return
while(Test!=0):
    Number_of_Spots=int(input())
    Spots = list(map(int, input().split()))
    cal(Spots)
    Test=Test-1