# https://www.codechef.com/JUNE20B/problems/EVENM

for _ in range(int(input())):
    n = int(input())
    label = 1
    if n % 2 == 1:  # odd
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print(label, end=" ")
                label += 1
            print()
    else:  # even
        odd = 1
        even = 2
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % 2 == 1:
                    if j % 2 == 1:
                        print(odd, end=" ")
                        odd += 2
                    else:
                        print(even, end=" ")
                        even += 2
                else:
                    if j % 2 == 1:
                        print(even, end=" ")
                        even += 2
                    else:
                        print(odd, end=" ")
                        odd += 2
            print()
