test, translation = map(str, input().split())
test = int(test)
hashtable = {}
byteland = "abcdefghijklmnopqrstuvwxyz"

punc = [".", ",", "?", "!"]
for i in range(len(translation)):
    if byteland[i] not in hashtable:
        hashtable[byteland[i]] = translation[i]
# print(hashtable)
for _ in range(test):
    sentence = input()
    decoded = ""
    for i in range(len(sentence)):
        if sentence[i].isupper():
            decoded = decoded + hashtable[sentence[i].lower()].upper()
        elif sentence[i] in punc:
            decoded = decoded + sentence[i]
        elif sentence[i] == "_":
            decoded = decoded + " "
        else:
            decoded = decoded + hashtable[sentence[i]]
    print(decoded)
