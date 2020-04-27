#https://www.codechef.com/RC122020/problems/RECNDSTR
for i in range(int(input())):
    string=input()
    L1 = string[0 : 1] 
    L2 = string[1 :] 
    R1 = string[0 : len(string)-1] 
    R2 = string[len(string)-1 : ]
    LR=L2+L1
    RR=R2+R1
    if LR==RR:
        print("YES")
    else:
        print("NO")
