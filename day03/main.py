def main():
    input = None
    with open("input.txt") as f:
        input = f.readlines()

    print(part1(input))
    print(part2(input))


# Returns a list of numbers found in the input as well as their coordinates
def find_numbers(input):
    numbers_map = []
    # For each row
    for row_idx in range(len(input)):
        row = input[row_idx]
        # For each char in row
        col_idx = 0
        while col_idx < len(row):
            if row[col_idx].isdigit():
                og_col_idx = col_idx
                while row[col_idx + 1].isdigit():
                    col_idx += 1
                numbers_map.append([
                    int("".join(row[og_col_idx:col_idx + 1])), 
                    {
                        'x': [og_col_idx, col_idx],
                        'y': row_idx
                    }
                    ])
            col_idx += 1
    return numbers_map

def part1(input):
    numbers_map = find_numbers(input)
    symbols = "!@#$%^&*()_+{}|:\"<>?`-=[]\;',/"
    part_numbers = []
    for number in numbers_map:
        y = number[1]['y']
        x = [number[1]['x'][0], number[1]['x'][1]]
        
        # Check left
        if x[0] > 0:
            # decrease x_range (will be used when checking other rows)
            x[0] -= 1
            if input[y][x[0]] in symbols:
                part_numbers.append(number[0])

        # Check right
        if x[1] < len(input[y]) - 1:
            # increase x_range (will be used when checking other rows)
            x[1] += 1
            if input[y][x[1]] in symbols:
                part_numbers.append(number[0])

        # Check above
        if y > 0:
            for idx in range(x[0] , x[1] + 1):
                if input[y - 1][idx] in symbols:
                    part_numbers.append(number[0])

        # Check below
        if y < len(input) - 1:
            for idx in range(x[0] , x[1] + 1):
                if input[y + 1][idx] in symbols:
                    part_numbers.append(number[0])
        
    return sum(part_numbers)

def part2(input):
    numbers_map = find_numbers(input)
    ties = []
    gear_ratio = 0 

    for row_idx in range(len(input)):
        row = input[row_idx]
        for col_idx in range(len(row)):
            if row[col_idx] == '*':
                ties.append([col_idx, row_idx])
    
    for tie in ties:       
        
        tied_nums = []
        for number in numbers_map:
            # Check left/right
            if tie[1] == number[1]['y']: 
                if (
                    number[1]['x'][0] == tie[0] + 1 or
                    number[1]['x'][1] == tie[0] - 1
                ):
                    tied_nums.append(number[0])
        
            # check top/bottom
            if (
                number[1]['y'] == tie[1] - 1 or
                number[1]['y'] == tie[1] + 1
            ):
                if tie[0] in range(number[1]['x'][0] - 1, number[1]['x'][1] + 2):
                    tied_nums.append(number[0])

        if len(tied_nums) > 1:
            prod = 1
            for num in tied_nums:
                prod *= int(num)
            gear_ratio += prod

    return(gear_ratio)

main()