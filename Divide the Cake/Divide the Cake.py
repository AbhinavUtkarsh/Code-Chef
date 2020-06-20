# https://www.codechef.com/problems/ANUDTC
for _ in range(int(input())):
    cuts = int(input())

    if 360 % cuts == 0:
        print("y", end=" ")
    else:
        print("n", end=" ")
    if cuts <= 360:
        print("y", end=" ")
    else:
        print("n", end=" ")
    if (cuts * (cuts + 1) / 2) <= 360:
        print("y", end=" ")
    else:
        print("n", end=" ")
    print()

