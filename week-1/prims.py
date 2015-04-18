def prims_min_span_tree(nodes_edge):
    # until considered = all points
    #   add all edges going out of considered to array
    #   find lowest edge and add node to considered
    #   increment total sum
    span_length = 0
    # choose random vertex and add it to set of considered points
    considered = filter(lambda x: x[0] == 1, nodes_edge)
    included_set = [1]
    print considered 
    print "is considered initially\n"

    max_node = max(map(lambda x: x[0], nodes_edge))
    print str(max_node) + "is max node\n"
   # return

    edge_count = len(nodes_edge)
    while len(included_set) < 442:
#    while len(included_set) < max_node:
        min_node = find_lowest_node(considered)
        print min_node 
        print "is min node\n"
        new_nodes = filter(lambda x: x[0] == min_node[1], nodes_edge)
        if len(new_nodes) == 0:
            considered.append([min_node[1], None, None])
        else:
            considered.extend(new_nodes)
#        print considered 
#        print "is considered\n"
        span_length += min_node[2]
        included_set.append(min_node[1])
        print str(span_length) + " is span length\n"

def find_lowest_node(nodes):
    included_nodes = set(map(lambda x: x[0], nodes))
    print included_nodes
    print 'is included nodes length\n'
    min_node = nodes[0]
    nodes_copy = list(nodes)
    for node in nodes_copy:
        if node[1] in included_nodes:
            None
#            nodes_copy.remove(node)
#            print "%(s)s %(t)s in included nodes\n" % {'s': node[0], 't': node[1]}
        else:
#            print "comparing %(val1)s against %(val2)s" % {'val1': str(node[0]) + ', ' + str(node[1]) + ': ' + str(node[2]), 'val2': min_node[2]}
            if node[2] < min_node[2] and node[2] <> None:
                min_node = node
    return min_node

def read_nodes_edge_file(file):
    nodes_edge = []
    with open(file, 'r') as f:
        nodes_edge = f.read().split('\n')
    f.closed
    nodes_edge = [elem.split(' ') for elem in nodes_edge][1:-1]
    return [[int(num) for num in elem] for elem in nodes_edge]

nodes_edge = read_nodes_edge_file('edges.txt')
prims_min_span_tree(nodes_edge)
