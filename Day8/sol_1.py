with open("input.txt", "r") as f:
    T = int(f.readline().strip())
    directions = list(f.readline().strip())
    f.readline()
    
    positions = {}

    for i in range(T):
        pos = f.readline().strip().split()
        positions[pos[0]] = pos[1:]

pos = "AAA"
count = 0

while pos != "ZZZ":
    match directions[count % len(directions)]:
        case "L":
            pos = positions[pos][0]
        case "R":
            pos = positions[pos][1]
    count += 1

print(pos, count)
