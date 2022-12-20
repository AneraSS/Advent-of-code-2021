# binary_number = "1101"
# decimal_number = binary_to_decimal(binary_number)
# print(decimal_number) # Output: 13
def binary_to_decimal(binary): # from stirng
    """Converts binary to decimal."""
    return int(binary, 2)

def strip_lines(lines):
    """Takes and returns list of strings, but without '\n at the end of a string."""
    stripped_lines = []
    for line in lines:
        stripped_line = line.strip('\n')
        stripped_lines.append(stripped_line)
    return stripped_lines


def initialize_list_of_lists(length):
    # create main list that has the length of first line
    main_list = []
    # initialize empty main list containing mini lists: [[],[],etc.]
    for i in range(0, length):
        main_list.append([])
    return main_list

with open('input.txt') as file_object:
    lines = strip_lines(file_object.readlines())
    main_list = initialize_list_of_lists(len(lines[0]))

    # filling out the main_list with mini_lists (columns)
    for line in lines:
        for i in range(0,len(line)):
            main_list[i].append(line[i])

    # generate gamma and epsilon ray as binary system
    gamma_ray = ""
    epsilon_ray = ""
    for i in range(0, len(main_list)):
        current_mini_list = main_list[i]
        count0 = 0
        count1 = 0
        for digit in current_mini_list:
            if digit == '0':
                count0 += 1
            if digit == '1':
                count1 += 1
        if count1 > count0:
            gamma_ray += "1"
            epsilon_ray += "0"
        elif count1 < count0:
            gamma_ray += "0"
            epsilon_ray += "1"

     # convert gamma and epsilon rate as decimal
    gamma_ray = binary_to_decimal(gamma_ray)
    epsilon_ray = binary_to_decimal(epsilon_ray)

print(gamma_ray*epsilon_ray)

# input obtained - 1071734