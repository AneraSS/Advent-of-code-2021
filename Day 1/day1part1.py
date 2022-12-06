with open ('input.txt') as file_object:
    full_list = []
    for line in file_object:
        line = int(line.strip('\n'))
        full_list.append(line)

    increase_counter = 0
    previous_number = full_list[0]
    for current_number in full_list:
        if current_number > previous_number:
            increase_counter += 1
            previous_number = current_number
        previous_number = current_number        # bc if-statement is False, then you still need to increase it
print(increase_counter)