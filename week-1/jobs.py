def sort_by_difference(weight_length):
    differences = zip(range(0,len(weight_length)), [int(elem[0]) - int(elem[1]) for elem in weight_length], [int(elem[0]) for elem in weight_length], [int(elem[1]) for elem in weight_length])
    sorted_diff = sorted(differences, key=lambda x: (x[1], x[2]), reverse=True)
    return sorted_diff

def sort_by_quotient(weight_length):
    quotients = zip(range(0, len(weight_length)), [float(elem[0])/float(elem[1]) for elem in weight_length], [int(elem[0]) for elem in weight_length], [int(elem[1]) for elem in weight_length])
    sorted_quotient = sorted(quotients, key=lambda x: x[1], reverse=True)
    return sorted_quotient

def get_total_weight(sorted_diff):
    weight = 0
    time = 0
    for elem in sorted_diff:
        time = time + elem[3]
        weight = weight + time * elem[2]
    return weight


def get_weight_length(file):
    weight_length = []
    with open(file, 'r') as f:
        weight_length = f.read().split('\n')
    f.closed

    weight_length = [elem.split(' ') for elem in weight_length][1:-1]
    return weight_length


weight_length = get_weight_length('jobs.txt')
sorted_diff = sort_by_difference(weight_length)
print get_total_weight(sorted_diff)

sorted_quotient = sort_by_quotient(weight_length)
# print sorted_quotient
print get_total_weight(sorted_quotient)
