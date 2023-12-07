hand_priorities = {
        'five_of_a_kind': 1,
        'four_of_a_kind': 2,
        'full_house': 3,
        'three_of_a_kind': 4,
        'two_pair': 5,
        'one_pair': 6,
        'high_card': 7
    }

def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
    
    print(part1(input))
    print(part2(input))


def part1(input):
    hands_by_type, hand_bids = get_hand_types_and_bids(input)
    hands_by_priority = get_hands_by_priority(hands_by_type)
    
    return calc_winnings(hands_by_priority, hand_bids)

def part2(input):
    hands_by_type, hand_bids = get_hand_types_and_bids(input, joker=True)
    hands_by_priority = get_hands_by_priority(hands_by_type, joker=True)
    
    return calc_winnings(hands_by_priority, hand_bids)
    
def hand_sort(elem, joker=False):
    card_face_vals = {
        'A': 14, 
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2   
    }

    if joker:
        card_face_vals['J'] = 1

    return [card_face_vals[char] for char in elem]         

def get_hand_types_and_bids(input, joker=False):
    hands_by_type = { 7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    hand_bids = {}
    for hand in input:        
        hand, bid = hand.split()
        joker_hand = replace_j(hand)
        hand_bids[hand] = bid
        if joker:
            card_counts = {val:list(joker_hand).count(val) for val in list(joker_hand)}
        else:
            card_counts = {val:list(hand).count(val) for val in list(hand)}
        
        match len(card_counts):
            case 5:
                hands_by_type[hand_priorities['high_card']].append(hand)
            case 4:
                hands_by_type[hand_priorities['one_pair']].append(hand)
            case 3:
                if 3 in card_counts.values():
                    hands_by_type[hand_priorities['three_of_a_kind']].append(hand)
                else:
                    hands_by_type[hand_priorities['two_pair']].append(hand)
            case 2:
                if 4 in card_counts.values():
                    hands_by_type[hand_priorities['four_of_a_kind']].append(hand)
                else:
                    hands_by_type[hand_priorities['full_house']].append(hand)
            case 1:
                hands_by_type[hand_priorities['five_of_a_kind']].append(hand)
    
    return hands_by_type, hand_bids

def get_hands_by_priority(hands_by_type, joker=False):
    hands_by_priority = []
    for type in hands_by_type:
        if len(hands_by_type[type]) == 1:
            hands_by_priority.append(hands_by_type[type][0])
        elif len(hands_by_type[type]) > 1:
            sorted_hands = sorted(hands_by_type[type], key=lambda hand: hand_sort(hand, joker))
            for hand in sorted_hands:
                hands_by_priority.append(hand)
    
    return hands_by_priority

def calc_winnings(hands_by_priority, hand_bids):
    winnings = 0
    for hand_idx in range(len(hands_by_priority)):
        winnings += (int(hand_bids[hands_by_priority[hand_idx]]) * (hand_idx + 1))

    return winnings

def replace_j(hand):
    card_counts = {val:list(hand).count(val) for val in list(hand)}
    highest_count = { 'type': 'null', 'count': 0 }
    for count in card_counts:
        if card_counts[count] > highest_count['count'] and count != 'J':
            highest_count['type'] = count
            highest_count['count'] = card_counts[count]
    
    return(hand.replace('J', highest_count['type']) if highest_count['type'] != 'null' else hand) 

main()