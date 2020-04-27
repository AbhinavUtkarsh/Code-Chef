#https://www.codechef.com/problems/CSUB
for i in range(int(input())):
    N=int(input())
    String=input()
    one_counter=0
    for i in String:
        if i=='1':
            one_counter=one_counter+1
    Total=(one_counter*(one_counter+1)/2)
    print(int(Total))