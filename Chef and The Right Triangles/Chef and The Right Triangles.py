#https://www.codechef.com/problems/RIGHTRI

def distance(x1,y1,x2,y2):
    return (((x1-x2)**2+(y1-y2)**2))
count=0
for i in range(int(input())):
    cord=list(map(int,input().split()))
    a = distance(cord[0],cord[1],cord[2],cord[3])
    b = distance(cord[0],cord[1],cord[4],cord[5])
    c = distance(cord[4],cord[5],cord[2],cord[3])
    hypo=(max(a,b,c))
    if hypo==a:
        if c+b==a:
            count+=1
    elif hypo==b:
        if c+a==b:
            count+=1
    elif hypo==c:
        if a+b==c:
            count=count+1
print(count)