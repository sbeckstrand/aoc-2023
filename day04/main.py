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
        points = 0
        wins = get_win_count(card)

        points += wins if wins <= 1 else pow(2, wins - 1)        
        total += points

    return int(total)

def part2(input):
    cards = input
    copies = {}
    for i in range(len(cards)):
        copies[i + 1] = 1

    for card_idx in range(1, len(cards)):
        for copy_count in range(copies[card_idx]):
            new_copies = get_win_count(cards[card_idx - 1])
            for i in range(card_idx + 1, card_idx + new_copies + 1):
                copies[i] = copies[i] + 1

    return sum(copies.values())

main()