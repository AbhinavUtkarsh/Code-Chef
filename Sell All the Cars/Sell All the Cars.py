#https://www.codechef.com/APRIL20B/problems/CARSELL
import numpy
Test=int(input())

while(Test!=0):
    N=int(input())
    Price = list(map(int, input().split()))
    Price=numpy.array(Price)
    Price=numpy.sort(Price)[::-1]
    for i in range(0,len(Price)):
        Price[i]=Price[i]-i
    Price[Price<0]=0
    print(sum(Price)%1000000007)
    Test=Test-1