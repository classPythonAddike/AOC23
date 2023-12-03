from typing import List, Tuple

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

parts: List[int] = []

for num in num_indices:
    is_part = False

    # Top and Bottom
    if num[0]:
        for i in range(num[1], num[2] + 1):
            if type(grid[num[0] - 1][i]) == str and grid[num[0] - 1][i] != '.':
                is_part = True
                break

    if num[0] != n - 1:
        for i in range(num[1], num[2] + 1):
            if type(grid[num[0] + 1][i]) == str and grid[num[0] + 1][i] != '.':
                is_part = True
                break

    # Left and Right

    if num[1]:
        if type(grid[num[0]][num[1] - 1]) == str and grid[num[0]][num[1] - 1] != '.':
            is_part = True

    if num[2] != n - 1:
         if type(grid[num[0]][num[2] + 1]) == str and grid[num[0]][num[2] + 1] != '.':
            is_part = True

    # Corners

    if num[0] and num[1]:
        if type(grid[num[0] - 1][num[1] - 1]) == str and grid[num[0] - 1][num[1] - 1] != '.':
            is_part = True

    if num[0] and num[2] != n - 1:
        if type(grid[num[0] - 1][num[2] + 1]) == str and grid[num[0] - 1][num[2] + 1] != '.':
            is_part = True

    if num[0] != n - 1 and num[1]:
        if type(grid[num[0] + 1][num[1] - 1]) == str and grid[num[0] + 1][num[1] - 1] != '.':
            is_part = True

    if num[0] != n - 1 and num[2] != n - 1:
        if type(grid[num[0] + 1][num[2] + 1]) == str and grid[num[0] + 1][num[2] + 1] != '.':
            is_part = True

    if is_part:
        parts.append(grid[num[0]][num[1]])

print(sum(parts))
