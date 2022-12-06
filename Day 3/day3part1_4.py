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
    # bc readlines gave [00100\n', '11110\n',...] , \n has to be removed
    for line in lines:
        stripped_line = line.strip('\n')

    counter_of_sets = 0 # to know how much sets were created
    gamma_ray = []
    epsilon_ray = []

    # create main list that has the length of first line
    main_list = [[]] * len(lines[0])
