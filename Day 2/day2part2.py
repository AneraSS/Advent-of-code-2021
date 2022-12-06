with open('input.txt') as file_object:
    instructions = []
    horizontal_position = 0
    aim = 0
    depth = 0
    for line in file_object:
        instruction = line.split(' ')
        motion = instruction[0]
        value = instruction[1]
        if motion == 'forward':
            horizontal_position += int(value)
            depth += aim*int(value)
        elif motion == 'down':
            aim += int(value)
        elif motion == 'up':
            aim -= int(value)
    multipyling = horizontal_position*depth
    print(multipyling)

# result obtained - 1864715580