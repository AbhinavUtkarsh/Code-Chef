# https://www.codechef.com/LTIME84B/problems/CONVSTR

for _ in range(int(input())):
    lengthOfString = int(input())
    a = input()
    b = input()
    if a == b:
        print(0)
        continue
    correctPositionHashTable = {}
    incorrectPositionHashTable = {}
    chosenElements = []
    resultMatrix = []
    for i in range(lengthOfString):
        if a[i] == b[i]:
            if a[i] not in correctPositionHashTable:
                correctPositionHashTable[a[i]] = [i]
            else:
                correctPositionHashTable[a[i]].append(i)
        else:
            if a[i] not in incorrectPositionHashTable:
                incorrectPositionHashTable[a[i]] = [i]
            else:
                incorrectPositionHashTable[a[i]].append(i)
    print(incorrectPositionHashTable)
    for i in incorrectPositionHashTable:
        for j in incorrectPositionHashTable[i]:
            chosenElements.append(j)
            if b[chosenElements[0]] in incorrectPositionHashTable:
                chosenElements.extend(incorrectPositionHashTable[b[chosenElements[0]]])
                if len(incorrectPositionHashTable[i]) == 1:
                    incorrectPositionHashTable[i] = []
                else:
                    del incorrectPositionHashTable[i][0]
                incorrectPositionHashTable[b[chosenElements[0]]] = []
            else:
                if len(incorrectPositionHashTable[i]) == 1:
                    incorrectPositionHashTable[i] = []
                else:
                    del incorrectPositionHashTable[i][0]
            print(b[chosenElements[0]])
            # try:
            #     del incorrectPositionHashTable[b[chosenElements[0]]]
            # except:
            #     pass
            resultMatrix.append(chosenElements)
    print(resultMatrix)
    print(correctPositionHashTable)
    print(incorrectPositionHashTable)
