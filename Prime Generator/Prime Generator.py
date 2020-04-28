#https://www.codechef.com/problems/PRIME1
for i in range(int(input())):
    lower_limit,upper_limit=map(int,input().split())
    hashtable={}
    for i in range(2,int(upper_limit**0.5)+1):
        for j in range(max(2,lower_limit//i),upper_limit//i+1):
            hashtable[i*j]=1
    for i in range(max(2,lower_limit),upper_limit+1):
        if i not in hashtable:
            print(i)
    print()