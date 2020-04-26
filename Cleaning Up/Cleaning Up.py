#https://www.codechef.com/problems/CLEANUP
for i in range(int(input())):
    #n not completed
    n,m=map(int,input().split())
    jobs_done=list(map(int,input().split()))
    chef=[]
    assis=[]
    flag=0
    for i in range(1,n+1):
        if i not in jobs_done and flag==0:
            chef.append(i)
            flag=1
        elif i not in jobs_done and flag==1:
            assis.append(i)
            flag=0
    for i in chef:
        print(i,end=" ")
    print()
    for i in assis:
        print(i,end=" ")
    print()