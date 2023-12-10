def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    print(part1(input))
    print(part2(input))

def build_plot_map(line):
    seq = [int(x) for x in line.split(" ")]
    plot_map = [seq]

    curr_index = 0
    while set(plot_map[-1]) != {0}:
        new_seq = []
        for i in range(len(plot_map[curr_index]) - 1):
            new_seq.append(plot_map[curr_index][i + 1] - plot_map[curr_index][i])
        
        plot_map.append(new_seq)
        curr_index += 1
    
    return plot_map
    
def part1(input):
    next_values = []
    for line in input:
        plot_map = build_plot_map(line)

        # Move back up the plot_map
        for i in range(1, len(plot_map) + 1):
            if i != len(plot_map):
                next_value = plot_map[-i][-1] + plot_map[-i - 1][-1]
                plot_map[-i - 1].append(next_value)
            else:
                next_values.append(plot_map[0][-1])

    return sum(next_values)

def part2(input):
    previous_values = []
    for line in input:
        plot_map = build_plot_map(line)
        
        # Move back up the plot_map
        for i in range(1, len(plot_map) + 1):
            if i != len(plot_map):
                previous_value = plot_map[-i - 1][0] - plot_map[-i][0]
                plot_map[-i - 1].insert(0, previous_value)
            else:
                previous_values.append(plot_map[0][0])

    return sum(previous_values)


main()