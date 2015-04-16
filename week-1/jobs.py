def schedule_by_difference(file):
    weight_length = []
    # make array of weight, length
    # make dictionary of differences
    # sort dictionary of differences by difference
    # use keys of sorted dictionary to return sum of weighted completion times
    with open(file, 'r') as f:
        weight_length = f.read().split('\n')
    f.closed

    weight_length = [elem.split(' ') for elem in weight_length][1:-1]
    differences = zip(range(0,len(weight_length)), [int(elem[0]) - int(elem[1]) for elem in weight_length], [int(elem[0]) for elem in weight_length], [int(elem[1]) for elem in weight_length])
    sorted_diff = sorted(differences, key=lambda x: (x[1], x[2]), reverse=True)

    weight = 0
    time = 0
    for elem in sorted_diff:
        time = time + elem[3]
        weight = weight + time * elem[2]

    return weight


print schedule_by_difference('jobs.txt')
