#https://www.codechef.com/problems/VOTERS
# def merge(array1,array2):
#     N1=len(array1)
#     N2=len(array2)
#     merged=[]
#     i,j=0,0
#     while(i<N1 and j<N2):
#         if array1[i]<array2[j]:
#             merged.append(array1[i])
#             i+=1
#         else:
#             merged.append(array2[j])
#             j+=1
#     merged=merged+array1[i:]+merged[j:]
#     return merged
N1,N2,N3=map(int,input().split())
hashy={}
for i in range(N1+N2+N3):
    i=int(input())
    if i in hashy.keys():
        hashy[i]+=1
    else:
        hashy[i]=1
voted=[]
for i in hashy.keys():
    if hashy[i]>=2:
        voted.append(i)
voted.sort()
print(len(voted))
for i in voted:
    print(i)   
# for i in range(0,N2):
#     list2.append(int(input()))
# for i in range(0,N3):
#     list3.append(int(input()))
# total=merge(list1,list2)
# total=merge(total,list3)
# voted=[]
# last=total[0]
# for i in range(1,len(total)):
#     if total[i]==last and total[i] not in voted :
#         voted.append(total[i])
#     last=total[i]
# print(len(voted))
# for i in voted:
#     print(i)
