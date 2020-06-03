# https://www.codechef.com/LTIME84B/problems/WWALK

for _ in range(int(input())):
    totalTime = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    weirdDistance = 0
    aliceLocation = 0
    bobLocation = 0
    for i in range(totalTime):
        if alice[i] == bob[i] and aliceLocation == bobLocation:
            weirdDistance += alice[i]
        aliceLocation += alice[i]
        bobLocation += bob[i]
    print(weirdDistance)
