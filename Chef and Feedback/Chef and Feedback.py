#https://www.codechef.com/problems/ERROR

for i in range(int(input())):
    string=input()
    if ("101" in string):
        print("Good")
    elif ("010" in string):
        print("Good")
    else:
        print("Bad")