import numpy as np

with open("input.txt", "r") as f:
    lines = [list(map(int, i.strip().split())) for i in f.readlines()]

sum_ = 0
for line in lines:
    a = np.array([
        [
            j ** i for i in range(len(line))
        ] for j in range(len(line))
    ], dtype=np.float64)
    
    x = np.linalg.solve(a, np.array(line, dtype=np.float64))
    sum_ += round(sum([x[i] * len(line) ** i for i in range(len(line))]), 5)

print(sum_)
