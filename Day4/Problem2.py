import os
from functools import cache

class Card:
    def __init__(self, line) -> None:
        card_id, card_data = line.split(": ")
        self.card_id = int(card_id.split()[1])

        winning_numbers, card_numbers = card_data.split(" | ")
        self.winning_numbers = [int(num) for num in winning_numbers.split()]
        self.card_numbers = [int(num) for num in card_numbers.split()]
    

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with open("input.txt", "r") as f: cards: tuple[Card] = tuple(Card(line) for line in f.read().splitlines())

    total_sum = len(cards) + sum(recursive_count(card, cards) for card in cards)

    print(total_sum)


@cache
def recursive_count(card: Card, cards: tuple[Card]) -> int:
    count = len(set(card.winning_numbers).intersection(set(card.card_numbers)))
    cards_subset = cards[card.card_id:card.card_id + count]
    return count + sum(recursive_count(each_card, cards) for each_card in cards_subset)

if __name__ == "__main__": main()