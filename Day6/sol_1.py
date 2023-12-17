with open("input.txt", "r") as f:
    times = map(int, f.readline().strip().split())
    distance = map(int, f.readline().strip().split())

    d = list(zip(times, distance))

# T, D - Race
# Hold button for t
# Distance = t * (T - t) > D
# t^2 - T * t + D < 0
# t => T +- sqrt(T * T - 4 * D) / 2
# t_min = ceil(T - sqrt(T * T - 4 * D) / 2)
# t_max = floor(T + sqrt(T * T - 4 * D) / 2)
# num_t = t_max - t_min + 1

import math

prod = 1
for T, D in d:
    T_by_2 = T / 2
    det = math.sqrt(T * T - 4 * D) / 2
    prod *= math.floor(T_by_2 + det - 0.0000001) - math.ceil(T_by_2 - det + 0.0000001) + 1

print(prod)
