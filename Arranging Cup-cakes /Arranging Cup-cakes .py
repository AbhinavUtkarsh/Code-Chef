# #https://www.codechef.com/problems/RESQ

# def isprime(num):
#     for i in range(2,int(pow(num,0.5)+1)):
#         if num%i==0:
#             return False
#     else:
#         return True

# def getfactors(num):
#     factors=[]
#     if isprime(num):
#         return [1,num]
#     else:
#         for i in range(2,num+1):
#             if num%i==0:
#                 factors.append(i)
#         return factors

# def perfectsquare(num):
#     if int(pow(num,0.5))*int(pow(num,0.5))==num:
#         return True
#     else:
#         return False
# for i in range(int(input())):
    
#     N=int(input())
#     if perfectsquare(N):
#         print("0")
#     else:
#         factors=getfactors(N)
#         diff=[]
#         for i in range(len(factors)-1):
#             diff.append(factors[i+1]-factors[i])
#         print(min(diff))

for _ in range(int(input())):
    
    N=int(input())
    
    flag_min=N-1
    for i in range(2,int(pow(N,0.5))+1):
        if N%i==0:
            if abs(((N//i)-i))<flag_min:
                flag_min=abs((N//i-i))
    print(flag_min)