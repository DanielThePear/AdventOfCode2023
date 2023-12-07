import os
import collections
from functools import cmp_to_key


card_values = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    sorted_lines = sorted(lines, key=cmp_to_key(custom_sorting_func))

    result = sum(
        i * int(each.split()[1])
        for i, each in enumerate(sorted_lines, 1)
    )

    print(result)
    

def custom_sorting_func(line_0, line_1) -> int:
    line_0_hand = line_0.split()[0]
    line_1_hand = line_1.split()[0]

    line_0_hand_type = identify_hand_type(line_0_hand)
    line_1_hand_type = identify_hand_type(line_1_hand)

    if line_0_hand_type != line_1_hand_type: return 1 if line_0_hand_type > line_1_hand_type else -1
    return compare_hands(line_0_hand, line_1_hand)

    
def compare_hands(hand_0, hand_1):
    for i in range(5):
        hand_0_char_val = card_values[hand_0[i]]
        hand_1_char_val = card_values[hand_1[i]]

        if hand_0_char_val == hand_1_char_val: continue
        return 1 if hand_0_char_val > hand_1_char_val else -1


def identify_hand_type(hand):
    # In-depth analysis of why this function does what it does can be found in "Types of Hands Analysis.md"
    match len(set(hand)):
        case 5: return 1 # High Card

        case 4: return 2 # One Pair
        
        case 3: # either Two Pair or Three of a Kind
            if collections.Counter(hand).most_common(1)[0][1] == 3: return 4 # Three of a kind
            return 3 # Two Pair
        
        case 2: # either Full House or Four of a Kind
            if collections.Counter(hand).most_common(1)[0][1] == 3: return 5 # Full house
            return 6 # Four of a Kind
        
        case 1: return 7 # Five of a Kind


if __name__ == "__main__": main()