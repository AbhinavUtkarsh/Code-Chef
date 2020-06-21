for _ in range(int(input())):
    string = input()
    stack = 0
    counter = 0
    for i in range(len(string)):

        if string[i] == "<":
            stack += 1
        else:
            stack -= 1
            if stack == 0:
                counter = max(counter, i + 1)
            elif stack < 0:
                break
    print(counter)
