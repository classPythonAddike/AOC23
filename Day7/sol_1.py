with open("input.txt", "r") as f:
    hands = {
        i.strip().split()[0].translate(
            {ord(i): ord(j) for i, j in {"T": ":", "J": ";", "Q": "<", "K": "=", "A": ">"}.items()}
        ): int(i.strip().split()[1])
        for i in f.readlines()
    }

hands_ordered_type = [{}, {}, {}, {}, {}, {}, {}]

for hand in hands:
    unique = set(hand)
    n_unique = len(unique)

    match n_unique:
        case 1:
            # 5 of a kind
            hands_ordered_type[0][hand] = hands[hand]
        case 2:
            # 4 of a kind
            if sorted([hand.count(i) for i in unique]) == [1, 4]:
                hands_ordered_type[1][hand] = hands[hand]
            # Full house
            elif sorted([hand.count(i) for i in unique]) == [2, 3]:
                hands_ordered_type[2][hand] = hands[hand]
        case 3:
            # 3 of a kind
            if sorted([hand.count(i) for i in unique]) == [1, 1, 3]:
                hands_ordered_type[3][hand] = hands[hand]
            # 2 pair
            elif sorted([hand.count(i) for i in unique]) == [1, 2, 2]:
                hands_ordered_type[4][hand] = hands[hand]
        case 4:
            # 1 pair
            hands_ordered_type[5][hand] = hands[hand]
        case 5:
            # High card
            hands_ordered_type[6][hand] = hands[hand]

ordered_hands = []

for hand_type in hands_ordered_type:
    for hand in sorted(hand_type.keys(), reverse=True):
        ordered_hands.insert(0, hand_type[hand])

print(sum([(i + 1) * j for i, j in enumerate(ordered_hands)]))
