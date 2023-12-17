with open("input.txt", "r") as f:
    cards = list(map(str.strip, f.readlines()))

score = 0
for card in cards:
    winning = set(map(int, card.split(":")[1].split("|")[0].split()))
    elf = set(map(int, card.split(":")[1].split("|")[1].split()))

    if l := len(winning.intersection(elf)):
        score += 2 ** (l - 1)

print(score)
