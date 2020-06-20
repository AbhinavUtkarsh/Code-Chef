# https://www.codechef.com/problems/PCYCLE
size = int(input())
permutation = list(map(int, input().split()))

cycles = []  # maintaining all the cycles
visited = []  # for checking if the current element is visited or not

for i in range(size):  # looping through the permutation array
    if i + 1 not in visited:  # checking if the element is already visited or not
        cycle = []  # for maitaining the each cycle
        while i + 1 not in cycle:  # to check if the start and end are now same or not
            cycle.append(i + 1)  # appending the individual cycle element
            visited.append(i + 1)  # making the same element visited
            i = permutation[i] - 1  # jumping to the next cycle element
        cycle.append(i + 1)  # appending the start element
        cycles.append(cycle)  # finally appending the local cycle itself
print(len(cycles))
for i in cycles:
    print(*i)

