def knapsack(txt_file):
    f = open(txt_file)

    first_line = f.readline().split(' ')
    knapsack_size = int(first_line[0])
    number_of_items = int(first_line[1][:-1])

    index = [] # double array with outer representing obj number and inner representing size of knapsack

    for item in range(number_of_items):
        print item
        line = f.readline().split(' ')
        value, weight = int(line[0]), int(line[1][:-1])
        if item <= 1:
            index.append([])
        else:
            index[1] = []
        for size in range(knapsack_size):
            if item == 0:
                if size + 1 < weight:
                    index[item].append(0)
                else:
                    index[item].append(value)
            else:
                if size + 1 < weight:
                    index[1].append(index[0][size])
                else:
                    if size - weight >= 0:
                        index[1].append(max(index[0][size], value + index[0][size - weight]))
                    else:
                        index[1].append(max(value, index[0][size]))
        if item > 0:
            index[0] = index[1]

    return index[1][size]
        
    
    # could only examine every 100 of knapsack space?
    




print knapsack('knapsack_big.txt')
