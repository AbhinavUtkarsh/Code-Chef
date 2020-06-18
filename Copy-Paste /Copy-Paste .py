for _ in range(int(input())):
    just_another_array_size = int(input())
    numbers = list(map(int, input().split()))
    print(len(set(numbers)))
