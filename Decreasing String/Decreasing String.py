for _ in range(int(input())):
    n = int(input())
    letters = "abcdefghijklmnopqrstuvwxyz"
    Qou = n // 25
    Rem = n % 25
    if Rem == 0:
        print(Qou * letters[::-1])
    else:
        print(letters[Rem::-1] + Qou * letters[::-1])
