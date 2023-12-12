
def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
    
    print(part1(input))
    print(part2(input))

def build_galaxy_map(input):
    inserts = {
        "rows": [],
        "cols": []
    }

    galaxy_count = 0
    galaxy_coords = {}

    # Expand galaxy cols
    for col in range(len(input[0])):
            col_list = [input[row][col] for row in range(len(input))]
            if set(col_list) == set("."):
                inserts["cols"].append(col)


    # Expand galaxy rows
    for row in range(len(input)):
        if set(input[row]) == set("."):
                inserts["rows"].append(row)

    # Replace # with numbers and build galaxy coordinate dict
    curr_galaxy = 1
    map = [list(row) for row in input]
    for row in range(len(map)):
        for col in range(len(input[row])):
            if input[row][col] == "#":
                map[row][col] = curr_galaxy
                galaxy_coords[curr_galaxy] = [row, col]
                curr_galaxy += 1
                galaxy_count += 1
    
    return galaxy_count, galaxy_coords, inserts

def get_distance(galaxy_count, galaxy_coords, inserts, expansion=2):
    pairs = []
    for i in range(galaxy_count):
        for j in range(i + 1, galaxy_count):
            pairs.append([i + 1, j + 1])
    
    total = 0
    for pair in pairs:
        # [ coords[0], coords[1], coords[2], coords[3]]
        counts = [0, 0, 0, 0]
        coords = [0, 0, 0, 0]

        coords[0], coords[1] = galaxy_coords[pair[0]]
        coords[2], coords[3] = galaxy_coords[pair[1]]

        for idx in inserts["rows"]:
            for coord in [0, 2]:
                if coords[coord]> idx:
                    counts[coord] += 1
        
        for idx in inserts["cols"]:
            for coord in [1, 3]:
                if coords[coord]> idx:
                    counts[coord] += 1

        for i in range(4):
            coords[i] = (coords[i] + counts[i] * expansion - counts[i]) if counts[i] > 0 else coords[i]
        
        total += abs(coords[2] - coords[0]) + abs(coords[3] - coords[1])

    return total

def part1(input):
    return get_distance(*build_galaxy_map(input))

def part2(input):
    return get_distance(*build_galaxy_map(input), expansion=1000000)

main()