from itertools import combinations

with open("input.txt", "r") as f:
    matrix = [list(i.strip()) for i in f.readlines()]

rows = []
columns = []

for j, i in enumerate(matrix):
    if set(i) == {"."}:
        columns.append(j)

matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for j, i in enumerate(matrix):
    if set(i) == {"."}:
        rows.append(j)

r_c = 0
for row in rows:
    matrix.insert(r_c + row, ["."] * len(matrix[0]))
    r_c += 1

matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

c_c = 0
for col in columns:
    matrix.insert(c_c + col, ["."] * len(matrix[0]))
    c_c += 1

galaxies = []
for row_n, row in enumerate(matrix):
    for col, p in enumerate(row):
        if p == "#":
            galaxies.append((row_n, col))

print(sum(abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]) for gal1, gal2 in combinations(galaxies, 2)))
