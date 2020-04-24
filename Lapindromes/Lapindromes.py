#https://www.codechef.com/LRNDSA01/problems/LAPIN

for _ in range(int(input())):
    String=input()
    if len(String)%2==0:
        Middle=len(String)//2
        Left=sorted(String[0:Middle])
        Right=sorted(String[Middle:])
        if Left==Right:
            print("YES")
        else:
            print("NO")
    else:
        Middle=len(String)//2+1
        Left=sorted(String[0:Middle-1])
        Right=sorted(String[Middle:])
        if Left==Right:
            print("YES")
        else:
            print("NO")
        