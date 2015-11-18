import collections

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
        
    
    # record weight:value pairs 

# def faster_knapsack(txt_file):
#     f = open(txt_file)
# 
#     first_line = f.readline().split(' ')
#     knapsack_size = int(first_line[0])
#     number_of_items = int(first_line[1][:-1])
# 
#     previous = collections.OrderedDict()
#     current = collections.OrderedDict()
# 
#     for item in range(number_of_items):
#         print item
#         line = f.readline().split(' ')
#         value, weight = int(line[0]), int(line[1][:-1])
#         
#         if item == 0:
#             if weight <= knapsack_size:
#                 current[weight] = value
#             else:
#                 current[knapsack_size] = 0
#         else:
#             prev_value = 0
#             for breakpoint in previous:
#                 if weight < breakpoint[0]:
#                     current[weight] = value
# 
#                 prev_value = breakpoint[1] # or whatever it should be






print knapsack('knapsack_big.txt')
