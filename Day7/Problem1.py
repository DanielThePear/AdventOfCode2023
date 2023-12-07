import os
import collections


def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    lines = merge_sort(lines)

    result = sum(
        i * int(each.split()[1])
        for i, each in enumerate(lines, 1)
    )

    print(result)
    

def custom_sorting_func(line_0, line_1) -> int:
    line_0_hand = line_0.split()[0]
    line_1_hand = line_1.split()[0]

    line_0_hand_type = identify_hand_type(line_0_hand)
    line_1_hand_type = identify_hand_type(line_1_hand)

    if line_0_hand_type != line_1_hand_type: return line_0_hand_type > line_1_hand_type
    return compare_hands(line_0_hand, line_1_hand)

    
def compare_hands(hand_1, hand_2):
    custom_values = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
    for i in range(5):
        hand_1_char_val = custom_values.index(hand_1[i])
        hand_2_char_val = custom_values.index(hand_2[i])

        if hand_1_char_val == hand_2_char_val: continue
        return hand_1_char_val > hand_2_char_val

def identify_hand_type(hand):
    if len(set(hand)) == 5: return 1 # High Card
    elif len(set(hand)) == 4: return 2 # One Pair
    elif len(set(hand)) == 3: # either Two Pair or Three of a Kind
        if collections.Counter(hand).most_common(1)[0][1] == 3: return 4 # Three of a kind
        else: return 3
    elif len(set(hand)) == 2: # either Full House or Four of a Kind
        if collections.Counter(hand).most_common(1)[0][1] == 3: return 5 # Full house
        else: return 6
    elif len(set(hand)) == 1: return 7 # Five of a Kind


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if custom_sorting_func(left[i], right[j]) == False:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


if __name__ == "__main__": main()