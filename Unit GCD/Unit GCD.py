#https://www.codechef.com/APRIL20B/problems/UNITGCD
import numpy as np

Test=int(input())

def Divisors(n) : 
    divs=[]
    i = 2
    while i <= n : 
        if (n % i==0) : 
            divs.append(i) 
        i = i + 1
    
    return divs

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

while(Test!=0):
    
    pages=int(input())
    all_pages=[i for i in range(2,pages+1)]
    total_days=pages//2
    Ans=[]
    for i in all_pages:
        if isprime(i):
            Ans.append(i)
        all_pages=list(set(all_pages)-set(Ans))
    for i in all_pages:
        master_flag=0
        divs=[]
        divs=Divisors(i)
        Ans.append(0)
        Ans.append(i)
        all_pages=list(set(all_pages)-set([i]))
        all_pages=sorted(all_pages)
        for j in all_pages:
            flag=0
            for k in divs:
                if(j%k)==0:
                    flag=1
                    break
            if(flag==0):
                master_flag=1
                Ans.append(j)
                divs.extend(Divisors(j))
                all_pages=list(set(all_pages)-set([j]))
                all_pages=sorted(all_pages)
    print(Ans) 
    Test=Test-1