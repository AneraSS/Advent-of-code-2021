with open ('test.txt') as file_object:
    full_list = []
    for line in file_object:
        line = int(line.strip('\n'))
        full_list.append(line)
    sum3 = 0
    new_list = []
    for i in range(0,len(full_list)):
        if len(full_list) >= 3:
            sum3 = full_list[0]+full_list[1]+full_list[2]
            new_list.append(sum3)
            full_list.pop(0)
            print(full_list)
            print(new_list)
        else:
            break

