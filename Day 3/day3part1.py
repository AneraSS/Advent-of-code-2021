with open('test.txt') as file_object:
    first_bit = []
    gamma_rate = []
    epsilon_rate = []
    for line in file_object:
        split_at = 1
        count0 = 0
        count1 = 0
        left, right = line[:split_at], line[split_at:]
        first_bit.append(left)
        file_object = right
    for bit in first_bit:
        if bit == '0':
            count0 += 1
        elif bit == '1':
            count1 += 1
        if count0 < count1:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        if count0 > count1:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    print(gamma_rate)