def main():
    input = None
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    print(part1(input, {'r': 12, 'g': 13, 'b': 14}))
    print(part2(input))

def part1(input, limit_cubes={'r': 0, 'g': 0, 'b': 0}):
    id_total = 0
    for game in input:
        id = game.split('Game ')[1].split(':')[0]
        handfuls = [handful.strip() for handful in game.split(':')[1].split(';')]
        max_cubes = {'r': 0, 'g': 0, 'b': 0}
        for handful in handfuls:
            cubes_by_color = [group.strip() for group in handful.split(',')]
            for group in cubes_by_color:
                color = group.split(' ')[1][0]
                amount = int(group.split(' ')[0])
                if amount > max_cubes[color]:
                    max_cubes[color] = amount
        is_valid = True
        for color in limit_cubes:
            if max_cubes[color] > limit_cubes[color]:
                is_valid = False
        
        if is_valid:
            id_total += int(id)
    
    return id_total
            

def part2(input):
    power_total = 0
    for game in input:
        handfuls = [handful.strip() for handful in game.split(':')[1].split(';')]
        max_cubes = {'r': 0, 'g': 0, 'b': 0}
        for handful in handfuls:
            cubes_by_color = [group.strip() for group in handful.split(',')]
            for group in cubes_by_color:
                color = group.split(' ')[1][0]
                amount = int(group.split(' ')[0])
                if amount > max_cubes[color]:
                    max_cubes[color] = amount
        power = max_cubes['r'] * max_cubes['g'] * max_cubes['b']
        power_total += power
    
    return power_total

main()
