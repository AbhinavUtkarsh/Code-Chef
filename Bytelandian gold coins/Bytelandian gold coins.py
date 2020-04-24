#https://www.codechef.com/problems/COINS

array={}
array[0]=0
array[1]=1

def Bytelandian(coin):
    if coin in array:
        return array[coin]
    else:
        array[coin]=max(coin,(Bytelandian(coin//2) + Bytelandian(coin// 3)+ (coin//4)))
        return array[coin]


while True:
    
    try:
        coin=int(input())
        print(Bytelandian(coin))
    except:
        break