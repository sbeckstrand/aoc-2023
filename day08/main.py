from math import lcm

def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read().splitlines()

    print(count_steps(input))               # part 1
    print(count_steps(input, multi=True))   # part 2 

def count_steps(input, multi=False):
    map = {}
    dirs = input[0].strip()
    curr_pos = [] if multi else ["AAA"]
    pos_steps = []

    for line in input[2:]:
        key, value = line.split(" = ")
        if key[-1] == 'A':
            curr_pos.append(key)

        value = value.replace("(", '').replace(")", '').replace(",", ' ').split()
        map[key] = {}
        map[key]["L"] = value[0]
        map[key]["R"] = value[1]

    curr_dir = 0
    steps = 0
    while len(curr_pos) > 0:
        to_remove = []
        steps += 1
        for pos in curr_pos:
            try:
                new_pos = map[pos][dirs[curr_dir]]
            except KeyError:
                print("Invalid input for part 1")
                exit(1)
            if new_pos[-1] == 'Z':
                to_remove.append(pos)
            else:
                curr_pos[curr_pos.index(pos)] = new_pos
            
        curr_dir = curr_dir + 1 if len(dirs) > curr_dir + 1 else 0

        for pos in to_remove:
            pos_steps.append(steps)
            curr_pos.remove(pos)
        
    return (lcm(*pos_steps)) if multi else steps

main()