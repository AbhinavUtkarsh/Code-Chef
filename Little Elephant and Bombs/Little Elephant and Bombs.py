for _ in range(int(input())):
    n = int(input())
    string = input()
    save_count = 0
    for i in range(n):
        exploded = False
        if string[i] == "1":
            exploded = True
        if i != 0 and string[i - 1] == "1":
            exploded = True
        if i != len(string) - 1 and string[i + 1] == "1":
            exploded = True
        if exploded == False:
            save_count += 1
    print(save_count)

