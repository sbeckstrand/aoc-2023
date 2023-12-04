def main():
    input = None
    with open("input.txt") as f:
        input = f.readlines()
    
    print(part1(input))
    print(part2(input))

def get_win_count(card):
    winning_numbers, rolled_numbers = [set(x.split()) for x in card.split(":")[1].split("|")]
    wins = winning_numbers.intersection(rolled_numbers)

    return len(wins)

def part1(input):
    total = 0
    for card in input: 
        wins = get_win_count(card)  
        total += wins if wins <= 1 else pow(2, wins - 1) 

    return int(total)

def part2(cards):
    copies = {x: 1 for x in range(1, len(cards) + 1)}

    for card_idx in range(1, len(cards)):
        new_copies = get_win_count(cards[card_idx - 1])
        for incremented_copy in range(card_idx + 1, card_idx + new_copies + 1):
            copies[incremented_copy] += copies[card_idx]

    return sum(copies.values())

main()