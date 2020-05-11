# https://www.codechef.com/MAY20B/problems/CORUS

for _ in range(int(input())):
    n,q=map(int,input().split())
    string=input()
    queries=[]
    for i in range(q):
        queries.append(int(input()))
    hashtable={}
    for i in string:
        if i not in hashtable:
            hashtable[i]=1
        else:
            hashtable[i]+=1
    #print(hashtable)
    for i in queries:
        counter=0
        for j in hashtable:
            if hashtable[j]>i:
                counter=counter+hashtable[j]-i
        if i==0:
            print(n)
        elif i==1:
            print(n-len(hashtable))
        else:
            print(counter)
