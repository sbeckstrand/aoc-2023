def main():
    input = None
    with open("ex-input.txt") as f:
        input = [x for x in f.read().split("\n\n") if len(x) > 0]
    print(part1(input))

def build_almanac(input):
    
    almanac = {}
    for section in input[1:]:
        title, vals = section.split(":")
        almanac[title.replace(" map", "")] = [x.split() for x in vals.split("\n") if len(x) > 0]

    return almanac

def build_seed_map(seeds, almanac):
    seed_map = { 'seed': {}}
    for seed in seeds:
        seed_map['seed'][int(seed)] = None
    
    for title, charts in almanac.items():
        src, dst = title.split("-to-")
        if seed_map.get(dst) is None:
            seed_map[dst] = {}
        for chart in charts:
            dst_val, src_val, chart_range = [int(x) for x in chart]
            for src_key, src_item in seed_map[src].items():
                if src_key in range(src_val, src_val + chart_range):
                    diff  = src_key - src_val

                    seed_map[src][src_key] = dst_val + diff
                    seed_map[dst][dst_val + diff] = None
                else:
                    if seed_map[src][src_key] is None:
                        seed_map[src][src_key] = src_key
                    seed_map[dst][src_key] = None
        
    return seed_map

def get_lowest_location(seeds, seed_map):
    lowest_location = None
    for seed in [int(x) for x in seeds]: 
        location = seed_map['humidity'][seed_map['temperature'][seed_map['light'][seed_map['water'][seed_map['fertilizer'][seed_map['soil'][seed_map['seed'][seed]]]]]]]

        if lowest_location is None or location < lowest_location:
            lowest_location = location
    
    return lowest_location

def part1(input):
    seeds = input[0].split(":")[1].split()
    almanac = build_almanac(input)
    seed_map = build_seed_map(seeds, almanac)
    
    lowest_location = get_lowest_location(seeds, seed_map)

    return(lowest_location)


main()