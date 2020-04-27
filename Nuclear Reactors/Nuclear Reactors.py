#https://www.codechef.com/problems/NUKES
A,N,K=map(int,input().split())
Chambers=[0 for i in range(K)]
N=N+1
for i in range(K):
   Chambers[i]=A%N
   A=A//N
   print(Chambers,i,A)
print(*Chambers)