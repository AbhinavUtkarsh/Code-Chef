#https://www.codechef.com/LRNDSA01/problems/ZCO14003

Customers=int(input())
Budget=[int(input()) for i in range(Customers)]
Budget.sort()
Max=0
index=0
for i in Budget:
    profit=i*(len(Budget)-index)
    if profit > Max:
        Max=profit
    index+=1

print(Max)