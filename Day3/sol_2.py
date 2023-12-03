from typing import List, Tuple, Dict

inp = open("input.txt", "r")
n = int(inp.readline().strip())

grid: List[List[int]] = [[]] * n
num_indices: List[Tuple[int, int, int]] = []

for i in range(n):
    line = inp.readline().strip()
    grid[i] = list(line)

    j = 0;
    num_ind = j
    while j < n:
        if line[j].isdigit():
            num_ind = j
            num = int(line[j])
            j += 1
            while j < n and line[j].isdigit():
                num = num * 10 + int(line[j])
                j += 1
            
            num_indices.append((i, num_ind, j - 1))
            for k in range(num_ind, j):
                grid[i][k] = num
        else:
            j += 1

gears: Dict[Tuple[int, int], List[int]] = {(i, j) : [] for i in range(n) for j in range(n)}

for num in num_indices:
    p_num = grid[num[0]][num[1]]
    # Top and Bottom
    if num[0]:
        for i in range(num[1], num[2] + 1):
            if grid[num[0] - 1][i] == '*':
                gears[(num[0] - 1, i)].append(p_num)

    if num[0] != n - 1:
        for i in range(num[1], num[2] + 1):
            if grid[num[0] + 1][i] == '*':
                gears[(num[0] + 1, i)].append(p_num)

    # Left and Right

    if num[1]:
        if grid[num[0]][num[1] - 1] == '*':
            gears[(num[0], num[1] - 1)].append(p_num)

    if num[2] != n - 1:
         if grid[num[0]][num[2] + 1] == '*':
            gears[(num[0], num[2] + 1)].append(p_num)

    # Corners

    if num[0] and num[1]:
        if grid[num[0] - 1][num[1] - 1] == '*':
            gears[(num[0] - 1, num[1] - 1)].append(p_num)

    if num[0] and num[2] != n - 1:
        if grid[num[0] - 1][num[2] + 1] == '*':
            gears[(num[0] - 1, num[2] + 1)].append(p_num)

    if num[0] != n - 1 and num[1]:
        if grid[num[0] + 1][num[1] - 1] == '*':
            gears[(num[0] + 1, num[1] - 1)].append(p_num)

    if num[0] != n - 1 and num[2] != n - 1:
        if grid[num[0] + 1][num[2] + 1] == '*':
            gears[(num[0] + 1, num[2] + 1)].append(p_num)

gears = {i: gears[i][0] * gears[i][1] for i in gears if len(gears[i]) == 2}
print(sum(gears.values()))
