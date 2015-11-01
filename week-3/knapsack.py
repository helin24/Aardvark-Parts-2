def knapsack(txt_file):
    f = open(txt_file)

    first_line = f.readline().split(' ')
    knapsack_size = int(first_line[0])
    number_of_items = int(first_line[1][:-1])

    index = [] # double array with outer representing obj number and inner representing size of knapsack

    for item in range(number_of_items):
        line = f.readline().split(' ')
        value, weight = int(line[0]), int(line[1][:-1])
        index.append([])
        for size in range(knapsack_size):
            if item == 0:
                if size + 1 < weight:
                    index[item].append(0)
                else:
                    index[item].append(value)
            else:
                if size + 1 < weight:
                    index[item].append(index[item-1][size])
                else:
                    if size - weight >= 0:
                        index[item].append(max(index[item - 1][size], value + index[item - 1][size - weight]))
                    else:
                        index[item].append(max(value, index[item - 1][size]))

    return index[item][size]




print knapsack('knapsack1.txt')
