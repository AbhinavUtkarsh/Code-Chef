#https://www.codechef.com/problems/SALARY
for i in range(int(input())):
    Number_of_workers=int(input())
    salaries_of_the_workers=list(map(int,input().split()))
    print(sum(salaries_of_the_workers)-min(salaries_of_the_workers)*Number_of_workers)
    