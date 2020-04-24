#https://www.codechef.com/COOK117B/problems/MATBREAK
MOD=10 ** 9 + 7

for _ in range(int(input())):
    N,A=map(int,input().split())
    Sum_of_Products=0
    for i in range(N):
        Factor=pow(A,2*(i+1)-1,MOD)
        Sum_of_Products+=Factor
        if Sum_of_Products > MOD:
            Sum_of_Products %= MOD
        A*=Factor
        if A > MOD:
            A %= MOD
    print(Sum_of_Products % MOD)