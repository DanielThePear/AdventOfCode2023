import os
import collections
from functools import cmp_to_key


def main() -> None:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    lines_sorted = sorted(lines, key=cmp_to_key(custom_sorting_func))

    result = sum(
        i * int(each.split()[1])
        for i, each in enumerate(lines_sorted, 1)
    )

    print(result)


def custom_sorting_func(line_0, line_1) -> int:
    line_0_hand = line_0.split()[0]
    line_1_hand = line_1.split()[0]

    line_0_hand_type = identify_hand_type(line_0_hand)
    line_1_hand_type = identify_hand_type(line_1_hand)

    if line_0_hand_type != line_1_hand_type: return 1 if line_0_hand_type > line_1_hand_type else -1
    return compare_hands(line_0_hand, line_1_hand)


def compare_hands(hand_1, hand_2):
    custom_values = ("J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A")
    for i in range(5):
        hand_1_char_val = custom_values.index(hand_1[i])
        hand_2_char_val = custom_values.index(hand_2[i])

        if hand_1_char_val == hand_2_char_val: continue
        return 1 if hand_1_char_val > hand_2_char_val else -1


def identify_hand_type(hand):
    # In-depth analysis of why this function does what it does can be found in "Types of Hands Analysis.md"
    if "J" not in hand:
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
    
    hand_counter_data = collections.Counter(hand)
    j_count = hand_counter_data["J"]
    hand_counter = hand_counter_data.most_common(5)
    if hand_counter[0][0] == "J": hand_counter = hand_counter[1:] 

    if 1 <= j_count <= 2: return identify_hand_type(hand.replace("J", hand_counter[0][0])) # Replace J with most common char, and identify hand
    elif 3 <= j_count <= 4: return identify_hand_type(hand.replace("J", hand_counter[-1][0])) # Replace J with least common char, and identify hand
    else: return 7 # return value for Five of a Kind


if __name__ == "__main__": main()