with open("input.txt", "r") as f:
    T = int(f.readline().strip())
    directions = list(f.readline().strip())
    f.readline()
    
    positions = {}

    for i in range(T):
        pos = f.readline().strip().split()
        positions[pos[0]] = pos[1:]

pos = [i for i in positions if i[-1] == "A"]
count = [0] * len(pos)

print(pos)

for i in range(len(pos)):
    while pos[i][-1] != "Z":
        match directions[count[i] % len(directions)]:
            case "L":
                pos[i] = positions[pos[i]][0]
            case "R":
                pos[i] = positions[pos[i]][1]
        count[i] += 1

print(pos, count, [i % len(directions) for i in count])

import math

print(math.lcm(*count))
