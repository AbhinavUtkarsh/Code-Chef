# https://www.codechef.com/JUNE20B/problems/EOEO

for _ in range(int(input())):
    ts = int(input())
    binary = bin(ts)[2:]
    # print(binary)
    # print(int(binary, 2))
    JerryWins = 0
    if int(binary[len(binary) - 1]) == int(1):
        JerryWins = ts // 2
    else:
        binary = binary.strip("0")
        if len(binary) > 1:
            JerryWins = int(binary, 2) // 2
    print(JerryWins)
