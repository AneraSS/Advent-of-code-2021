with open ('input.txt') as file_object:
    full_list = []
    for line in file_object:
        line = int(line.strip('\n'))
        full_list.append(line)

    sum3 = 0
    new_list = []
    for i in range(0,len(full_list)-2): # bc with 2 last no it can't do a thing
        sum3 = full_list[i]+full_list[i+1]+full_list[i+2]
        new_list.append(sum3)

    increase_counter = 0
    previous_number = new_list[0]
    for current_number in new_list:
        if current_number > previous_number:
            increase_counter += 1
            previous_number = current_number
        previous_number = current_number        # bc if-statement is False, then you still need to increase it
print(increase_counter)

# result obtained - 1103