# https://www.codechef.com/problems/LOSTWKND
for _ in range(int(input())):
    hours = list(map(int, input().split()))
    multiplier = hours[len(hours) - 1]
    del hours[len(hours) - 1]
    for i in range(len(hours)):
        hours[i] = hours[i] * multiplier
    total_work_hours = sum(hours)
    if total_work_hours <= 120:
        print("No")
    else:
        print("Yes")
