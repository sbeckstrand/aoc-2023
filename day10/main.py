def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    print(part1(input))
    print(part2(input))

def build_maze_map(input):
    start = []
    connection_map = []
    start_connected = []

    connectors = {
        #pipeval: [row left, row right, col up, col down]
        "|": [[-1, 0], [1, 0]],
        "-": [[0, -1], [0, 1]],
        "L": [[-1, 0], [0, 1]],
        "J": [[-1, 0], [0, -1]],
        "7": [[0, -1], [1, 0]],
        "F": [[0, 1], [1, 0]]
    }

    # find start
    while(len(start) == 0):
        for row in range(len(input)):
            for col in range(len(input[row])):
                if input[row][col] == "S":
                    start = [row, col]
                    break

    for row in range(len(input)):
        connection_map.append([])
        for col in range(len(input[row])):
            val = input[row][col]
            if connectors.get(val):
                connected_spaces = []

                for coords in connectors.get(val):
                    connected = [row + coords[0], col + coords[1]]
                    if 0 <= connected[0] <= len(input) and 0 <= connected[1] <= len(input[row]):
                        connected_spaces.append(connected)
                    
                    if start == connected:
                        start_connected.append([row, col, 1])

                connection_map[row].append(connected_spaces)
            else:
                connection_map[row].append([])
    
    return start, start_connected, connection_map
    

       

            
def part1(input):
    start, queue, map = build_maze_map(input)
    highest_count = 0
    visited = [start]

    # test_map = [["." for x in range(len(input[0]))] for y in range(len(input))]


    while len(queue) > 0:
        row, col, step_count = queue.pop()
        highest_count = max(highest_count, step_count)
        # test_map[row][col] = step_count
        visited.append([row, col])

        # print(f'Queue: {queue}, Current: {[row, col, step_count]}, Visisted: {visited}, Connected: {map[row][col]}')
        for connected_tiles in [x for x in map[row][col] if x not in visited]:
            new_row, new_col, new_step_count = connected_tiles[0], connected_tiles[1], step_count + 1
            
            queue.insert(0, [new_row, new_col, new_step_count])
    
    # for row in test_map:
    #     print(row)

    return highest_count
def part2(input):
    pass

main()

