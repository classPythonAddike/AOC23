with open("input.txt", "r") as f:
    T = int(f.readline().replace(" ", "").strip())
    D = int(f.readline().replace(" ", "").strip())

# T, D - Race
# Hold button for t
# Distance = t * (T - t) > D
# t^2 - T * t + D < 0
# t => T +- sqrt(T * T - 4 * D) / 2
# t_min = ceil(T - sqrt(T * T - 4 * D) / 2)
# t_max = floor(T + sqrt(T * T - 4 * D) / 2)
# num_t = t_max - t_min + 1

import math

T_by_2 = T / 2
det = math.sqrt(T * T - 4 * D) / 2
print(math.floor(T_by_2 + det - 0.0000001) - math.ceil(T_by_2 - det + 0.0000001) + 1)
