import re

p = re.compile("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))")
d = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", "r") as f:
    inp = f.readlines()
    sum_ = 0

    for i in inp:
        i = i.strip()
        a = list(p.findall(i))
        for ind, j in enumerate(a):
            if j in d:
                a[ind] = str(d.index(j) + 1)

        s = ''.join(a)
        sum_ += int(s[0] + s[-1])
    
    print(sum_)
