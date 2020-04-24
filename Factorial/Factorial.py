#https://www.codechef.com/LRNDSA01/problems/FCTRL

for _ in range(int(input())):
    Number=int(input())
    Factorial_0=0
    Divide=5
    while(Number//Divide>=1):
        Factorial_0+=Number//Divide
        Divide*=5
    print(Factorial_0)