from typing import Tuple
from pprint import pprint as print
from functools import cmp_to_key

with open("input.txt", "r") as f:
    hands = {
        tuple(
            ord(l) - ord("0")
            for l in i.strip().split()[0].translate(
                {ord(k): ord(j) for k, j in {"T": ":", "J": "1", "Q": ";", "K": "<", "A": "="}.items()}
            )
        ): int(i.strip().split()[1])
        for i in f.readlines()
    }

hands_ordered_type = [{}, {}, {}, {}, {}, {}, {}]

def stronger_hand(a: Tuple[int], b: Tuple[int]) -> Tuple[int]:
    for i, j in zip(a, b):
        if i > j:
            return 1
        elif i < j:
            return -1

for raw_hand in hands:
    strongest_hand_type = 6 # High Card
    strongest_hand_unique = 5
    strongest_hand = raw_hand

    if raw_hand == (1, 1, 1, 1, 1):
        strongest_hand_type = 0
        strongest_hand_unique = 1
        strongest_hand = (13, 13, 13, 13, 13)
    
    for joker in set(raw_hand):
        if joker == 1:
            continue

        hand = tuple(joker if i == 1 else i for i in raw_hand)
        unique = set(hand)
        n_unique = len(unique)

        hand_type = 0

        match n_unique:
            case 1:
                # 5 of a kind
                hand_type = 0
            case 2:
                # 4 of a kind
                if sorted([hand.count(i) for i in unique]) == [1, 4]:
                    hand_type = 1
                # Full house
                elif sorted([hand.count(i) for i in unique]) == [2, 3]:
                    hand_type = 2
            case 3:
                # 3 of a kind
                if sorted([hand.count(i) for i in unique]) == [1, 1, 3]:
                    hand_type = 3
                # 2 pair
                elif sorted([hand.count(i) for i in unique]) == [1, 2, 2]:
                    hand_type = 4
            case 4:
                # 1 pair
                hand_type = 5
            case 5:
                # High card
                hand_type = 6

        if hand_type < strongest_hand_type or (hand_type == strongest_hand_type and stronger_hand(hand, strongest_hand) == 1):
            strongest_hand_type = hand_type
            strongest_hand_unique = n_unique
            strongest_hand = hand

    hands_ordered_type[strongest_hand_type][raw_hand] = hands[raw_hand]


ordered_hands = []

for hand_type in hands_ordered_type:
    for hand in sorted(hand_type.keys(), reverse=True, key=cmp_to_key(stronger_hand)):
        ordered_hands.insert(0, hand_type[hand])

print(sum([(i + 1) * j for i, j in enumerate(ordered_hands)]))
