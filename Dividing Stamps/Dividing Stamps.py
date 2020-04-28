#https://www.codechef.com/problems/DIVIDING
number_of_members=int(input())
listy=list(map(int,input().split()))
total=sum(listy)
stamps_index=((number_of_members)*(number_of_members+1))/2
if stamps_index==total:
    print("YES")
else:
    print("NO")

