#https://www.codechef.com/APRIL20B/problems/STRNO
import math

Test=int(input())
def PF(n): 
    Factors=[]
    while n % 2 == 0: 
        Factors.append(2) 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            Factors.append(i) 
            n = n / i 
    if n > 2: 
        Factors.append(n)
    return(len(Factors))

while(Test!=0):
    
    x, k = map(int,input().split())
    ret=PF(x)
    if(ret==k):
        print(1)
    else:
        print(0)
    Test=Test-1
