def main():
    input = None
    with open("input.txt") as f:
        input = f.readlines()
    
    print(part1(input))
    print(part2(input))

def part1(input):
    total = 0
    for card in input: 
        points = 0
        count = 0
        winning_numbers, rolled_numbers = [x.strip() for x in card.split(":")[1].split("|")]
        for number in rolled_numbers.split(" "):
            if number in winning_numbers.split(" ") and number != '':
                count += 1

        points += count if count <= 1 else pow(2, count - 1)        
        total += points

    return int(total)

# This recursive function is a bit slow, but it works. 
# Could be replaced with an iterative solution doing less work
def process_copies(start_index, copies, cards, total_copies):
    if copies == 0:
        return total_copies
    else: 
        max_range = start_index + copies if start_index + copies < len(cards) else len(cards)
        for idx in range(start_index, max_range):
            new_copies = 0
            total_copies += 1
            winning_numbers, rolled_numbers = [x.strip() for x in cards[idx].split(":")[1].split("|")]
            for number in rolled_numbers.split(" "):
                if number in winning_numbers.split(" ") and number != '':
                    new_copies += 1
                    
            total_copies = process_copies(idx + 1, new_copies, cards, total_copies)

        return total_copies

def part2(input):
    total = 0
    cards = input
    for card_idx in range(len(cards)):
        total += process_copies(card_idx, 1, cards, 0)
    return total

main()
