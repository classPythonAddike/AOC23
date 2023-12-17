with open("input.txt", "r") as f:
    cards = list(map(str.strip, f.readlines()))

new_cards = {}
for i, card in enumerate(cards):
    new_cards[i] = [card, 1]

for i in new_cards:
    card = new_cards[i][0]
    winning = set(map(int, card.split(":")[1].split("|")[0].split()))
    elf = set(map(int, card.split(":")[1].split("|")[1].split()))

    if l := len(winning.intersection(elf)):
        for j in range(i + 1, i + l + 1):
            new_cards[j][1] += new_cards[i][1]

print(sum([i[1] for i in new_cards.values()]))
