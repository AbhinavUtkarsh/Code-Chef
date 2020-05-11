#https://www.codechef.com/MAY20B/problems/CHANDF
import math 
def decimalToBinary(n):  
    return bin(n).replace("0b", "")
for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    p=0
    if x==0 or y==0:
        print("0")
        continue
    x_bi=decimalToBinary(x)
    y_bi=decimalToBinary(y)
    r_bi=decimalToBinary(r)
    xx=[]
    yy=[]
    c=[]
    if len(x_bi)>=len(y_bi):
        p=len(x_bi)
        count=len(x_bi)-len(y_bi)
        while(len(x_bi)!=0):
            xx.append(x_bi.pop())
        while(count!=0):
            yy.append(0)
            count=count-1
        while(len(y_bi)!=0):
            xx.append(y_bi.pop())
    else:
        p=len(y_bi)
        count=len(y_bi)-len(x_bi)
        while(len(y_bi)!=0):
            yy.append(y_bi.pop())
        while(count!=0):
            xx.append(0)
            count=count-1
        while(len(x_bi)!=0):
            xx.append(x_bi.pop())
    counter=p-len(r_bi)
    if counter>0:
        while(counter!=0):
            c.append(0)
            counter=counter-1
    while(len(r_bi)):
        c.append(r_bi.pop())
    ans=[]
    for i in range(p):
        ans.append(0)
    k=0
    t=0
    val1=0
    val2=0
    p1=0
    counting=0
    while(len(xx)!=0 and len(yy)!=0):
        counting=counting+1
        i1=0
        i2=0
        check1=0
        u1=
        
    