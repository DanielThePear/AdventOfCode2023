import os

def main() -> None:

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("input.txt", "r") as f: lines = f.read().splitlines()
    
    total_sum = 0
    for line in lines:
        winning_numbers, card_numbers = line.split(" | ")
        winning_numbers = [int(num) for num in winning_numbers.split(": ")[1].split()]
        card_numbers = [int(num) for num in card_numbers.split()]
        total_sum += round(2 ** (len(set(winning_numbers).intersection(set(card_numbers))) - 1))
        # so this is kinda funny but I forgot to cover the edge case of len() returning 0, so there are cases where the exponent is -1 and it adds 0.5 to the total sum.
        # round() gets rid of those edge cases
    
    print(total_sum)
        

if __name__ == "__main__": main()