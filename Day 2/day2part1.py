with open('input.txt') as file_object:
    instructions = []
    motion_forward = 0
    motion_down = 0
    for line in file_object:
        instruction = line.split(' ')
        motion = instruction[0]
        value = instruction[1]
        if motion == 'forward':
            motion_forward += int(value)
        elif motion == 'down':
            motion_down += int(value)
        elif motion == 'up':
            motion_down -= int(value)
    multipyling = motion_forward*motion_down
    print(multipyling)

# result obtained - 2215080