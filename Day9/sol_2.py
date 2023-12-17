with open("input.txt", "r") as f:
    lines = [list(map(int, i.strip().split())) for i in f.readlines()]

sum_ = 0
for line in lines:
    differences = [line]
    while any(line):
        line = [line[i] - line[i - 1] for i in range(1, len(line))]
        differences.append(line)

    differences[-1].append(0)

    for i in range(len(differences) - 1):
        differences[-i - 2].insert(0, differences[-i - 2][0] - differences[-i - 1][0])
    
    sum_ += differences[0][0]

print(sum_)
