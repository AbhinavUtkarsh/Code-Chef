# https://www.codechef.com/JUNE20B/problems/GUESSG

n = int(input())
grader = "X"

counter = 0  # for odd and even iterations

low_e = 0
high_e = n
low_o = 0
high_o = n
question_o = 0
question_e = 0


while grader != "E":
    counter += 1
    print("COUNTER: ", counter)
    if counter % 2 == 1:
        question_o = (low_o + high_o) // 2
        print(question_o)
        grader = input()
        if grader == "G":
            low_o = (low_o + high_o) // 2
        elif grader == "L":
            high_o = (low_o + high_o) // 2
    else:
        question_e = (low_e + high_e) // 2
        print(question_e)
        grader = input()
        if grader == "G":
            low_e = (low_e + high_e) // 2
        elif grader == "L":
            high_e = (low_e + high_e) // 2
