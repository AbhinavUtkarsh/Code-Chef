#https://www.codechef.com/MAY20B/problems/TWOSTRS
def count(string, substring): 
    Count = 0
    start = 0
    while start < len(string): 
        pos = string.find(substring, start) 
        if pos != -1: 
            start = pos + 1
            Count += 1
        else: 
            break
    return Count

for i in range(int(input())):
    string1=input()
    string2=input()
    n=int(input())
    powers={}
    min_power_element=99999999999
    for i in range(0,n):
        string=list(map(str,input().split()))
        powers[string[0]]=int(string[1])
        if len(string[0])<min_power_element:
            min_power_element=len(string[0])
    #print(min_power_element)
    s1_substrs=[""]
    s2_substrs=[""]
    sum_string=[]
    s1_substrs.extend([string1[i:j+1] for i in range(len(string1)) for j in range(i,len(string1))])
    s2_substrs.extend([string2[i:j+1] for i in range(len(string2)) for j in range(i,len(string2))])
    #print(s1_substrs)
    #print(s2_substrs)
    for i in range(len(string2)):
        for j in range(i+1,len(string2)+1):
            s2_substrs.append(string2[i: j])
    for i in range(len(s1_substrs)):
        for j in range(len(s2_substrs)):
            if len(s1_substrs[i]+s2_substrs[j])>=min_power_element:
                sum_string.append(s1_substrs[i]+s2_substrs[j])
    #print(sum_string)
    maxima=-99999999999
    for i in range(len(sum_string)):
        current=0
        for key, value in powers.items():
            if sum_string[i].count(key)>0:
                current=current+(count(sum_string[i],key)*(value))
            if current>=maxima:
                maxima=current
    print(maxima)