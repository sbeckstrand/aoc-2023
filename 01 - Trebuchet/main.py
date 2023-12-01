with open('input.txt') as f:
    lines = f.read().splitlines()

def part1(lines):
    line_vals = []

    for line in lines: 
        nums = []
        for char in line:
            if char.isdigit():
                nums.append(int(char))
        if len(nums) > 0:
            line_vals.append(int(f'{nums[0]}{nums[-1]}'))
        
    return sum(line_vals)

def part2(lines):
    digit_words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    line_vals = []
    
    for line in lines:
        nums = []

        for i in range(0, len(line)):
            char = line[i]
            digit_filtered = {k:v for (k,v) in digit_words.items() if char == k[0]}
            for word in digit_filtered.keys():
                if line[i:i+len(word)] == word:
                    nums.append(digit_filtered[word])
            
            if char.isdigit():
                nums.append(int(char))
        if len(nums) > 0:
            line_vals.append(int(f'{nums[0]}{nums[-1]}'))
        
    return(sum(line_vals))

print(part1(lines))
print(part2(lines))