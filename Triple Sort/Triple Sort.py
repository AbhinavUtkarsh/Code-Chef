#https://www.codechef.com/MAY20B/problems/TRPLSRT/
import time
from sys import stdin, stdout
import random
def binarySearch(arr, l, r, x): 
    while l <= r: 
        mid = l + (r - l) // 2; 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1
def get_non_sorted_min(array,triplet):
    for i in array:
        if i not in triplet:
            return i
    return -1
flag=0
for i in range(int(input())):
    n,k=map(int,input().split())
    integers=[int(x) for x in stdin.readline().split()]
    #print("INTS",integers)
    copy=sorted(integers)
    triplets=[]
    unsorted=[]
    for i in range(n):
        if i+1!=integers[i]:
            unsorted.append(i)
    while(len(triplets)<=k):
        if len(unsorted)<=2:
            print("-1")
            break
        else:
            triplet=[-1 for i in range(3)]
            triplet[0]=unsorted[0]
            triplet[1]=integers[unsorted[0]]-1
            if integers[triplet[1]]-1 not in triplet:
                triplet[2]=integers[triplet[1]]-1
            else:
                triplet[2]=get_non_sorted_min(unsorted,triplet)
                if triplet[2]==-1 and flag==0:
                    print("-1")
                    flag=1
                    break
            temp=integers[triplet[0]]
            integers[triplet[0]]=integers[triplet[2]]
            integers[triplet[2]]=integers[triplet[1]]
            integers[triplet[1]]=temp
            if integers[triplet[0]]==triplet[0]+1 and integers[triplet[1]]==triplet[1]+1 and integers[triplet[2]]==triplet[2]+1:
                t2=binarySearch(unsorted,0,len(unsorted)-1,triplet[2])
                del unsorted[t2]
                t1=binarySearch(unsorted,0,len(unsorted)-1,triplet[1])
                del unsorted[t1]
                del unsorted[0]
            elif integers[triplet[0]]==triplet[0]+1 and integers[triplet[1]]==triplet[1]+1:
                del unsorted[0]
                t1=binarySearch(unsorted,0,len(unsorted)-1,triplet[1])
                del unsorted[t1]
            elif integers[triplet[0]]==triplet[0]+1 and integers[triplet[2]]==triplet[2]+1:
                t2=binarySearch(unsorted,0,len(unsorted)-1,triplet[2])
                del unsorted[t2]
                del unsorted[0]
            elif integers[triplet[1]]==triplet[1]+1 and integers[triplet[2]]==triplet[2]+1:
                t2=binarySearch(unsorted,0,len(unsorted)-1,triplet[2])
                del unsorted[t2]
                t1=binarySearch(unsorted,0,len(unsorted)-1,triplet[1])
                del unsorted[t1]
            elif integers[triplet[0]]==triplet[0]+1:
                del unsorted[0]
            elif integers[triplet[1]]==triplet[1]+1:
                t1=binarySearch(unsorted,0,len(unsorted)-1,triplet[1])
                del unsorted[t1]
            elif integers[triplet[2]]==triplet[2]+1:
                t2=binarySearch(unsorted,0,len(unsorted)-1,triplet[2])
                del unsorted[t2]
            triplets.append(triplet)
            #print("TRIPLETS CHOSEN",triplet,"INTS",integers)
            #print("UNSORTED",unsorted,len(unsorted))
            if copy==integers and len(triplets)<=k:
                print(len(triplets))
                for i in triplets:
                    for j in i:
                        print(j+1,end=" ")
                    print()
                #print(len(unsorted),len(triplets))
                break
        if len(triplets)>(k) and flag==0:
            print("-1")
            break