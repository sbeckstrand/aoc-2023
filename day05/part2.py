def main():
    input = None
    with open("input.txt") as f:
        input = [x for x in f.read().split("\n\n") if len(x) > 0]
    print(part2(input))

def build_almanac(input):
    almanac = { 'sections': {}}
    seed_ranges = []
    i = 0
    while i < len(input[0].split(":")[1].split()):
        seed_start, seed_range = [int(x) for x in input[0].split(":")[1].split()[i:i+2]]
        seed_ranges.append([seed_start, seed_range])
        i += 2
    almanac['seed_ranges'] = seed_ranges
    
    for section in input[1:]:
        title, vals = section.split(":")
        almanac['sections'][title.replace(" map", "")] = [x.split() for x in vals.split("\n") if len(x) > 0]

    return almanac

def findLowest(almanac):
    lowest_location = None

    for seed_range in almanac['seed_ranges']:
        locationRanges = convertSeedtoLocation(seed_range, almanac['sections'])

        for locationRange in locationRanges:
            if lowest_location == None:
                lowest_location = locationRange[0]
            elif locationRange[0] < lowest_location:
                lowest_location = locationRange[0]
        
    return lowest_location

def convertSeedtoLocation(seed_range, categories):
    curr_ranges = [seed_range]

    for category in categories:
        new_ranges = []

        for range in curr_ranges:
            converted = convertRange(range, categories[category])

            for converted_range in converted:
                new_ranges.append(converted_range)

        curr_ranges = new_ranges
    
    return curr_ranges

def convertRange(range, category):
    start, length = range
    converted_ranges = []

    for chart in category:
        dst, src, chart_range = [int(x) for x in chart]
        src_end = src + chart_range

        if (start < src_end and start + length > src):
            overlap_start = max(start, src)
            overlap_end = min(start + length, src_end)
            new_sart = dst + (overlap_start - src)

            converted_ranges.append([new_sart, overlap_end - overlap_start])
    
    if len(converted_ranges) > 0:
        return converted_ranges
    else:
        return [[start, length]]

def part2(input):
    
    almanac = build_almanac(input)
    result = findLowest(almanac)

    return result
    
main()