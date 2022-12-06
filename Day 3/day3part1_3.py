def get_decima_from_binary(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)


with open('test.txt') as file_object:
    lines = file_object.readlines()
    print(lines)
    counter_of_sets = 0 # to know how much sets were created
    gamma_ray = []
    epsilon_ray = []

    # create main list that has the length of first line
    main_list = [[]] * len(lines[0])

    for line in lines:
        for i in range(0,len(line)):
            if main_list[i]:
            main_list[i].append(line[i])



            divide_at = i
            left, right = line[i:], line[:i]
            mini_set.append(left)
            line = right
            global_set.append()

    for i in sets:
        for 'set_{}'.format(i):
            count0 = 0
            count1 = 0
            for number in set:
                if number == 1:
                    count1 += 1
                if number == 0:
                    count0 +=1
            if count1 > count0:
                gamma_ray.append(1)
                epsilon_ray.append(0)
            elif count1 < count0:
                gamma_ray.append(0)
                epsilon_ray.append(1)
    # transform from binary to decimal:
    decimal_gamma_ray = get_decima_from_binary(gamma_ray)
    decimal_epsilon_ray = get_decima_from_binary(epsilon_ray)
    # calculate the result
    result = gamma_ray*epsilon_ray
print(result)
