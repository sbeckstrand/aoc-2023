def main():
    input = None
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    
    print(part1(input))
    print(part2(input))

def find_faster_times(races):
    total = 1
    for race in races: 
        
        faster_times = 0
        for i in range(0, race['time']):
            pace = i
            distance = (race['time'] - i) * pace
            
            if distance > race['distance']:
                faster_times += 1

        total *= faster_times
    
    return total

def part1(input):
    races = []
    times = input[0].split(":")[1].split()
    distances = input[1].split(":")[1].split()
    for i in range(len(times)):
        races.append({
            "time": int(times[i]),
            "distance": int(distances[i]),
        })
    
    return(find_faster_times(races))
    
def part2(input):
    races = [{
        'time': int(input[0].split(":")[1].replace(" ","")),
        'distance': int(input[1].split(":")[1].replace(" ",""))
    }]

    return(find_faster_times(races))

main()