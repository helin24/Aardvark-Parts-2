def prims_min_span_tree(nodes_edge):
    # until considered = all points
    #   add all edges going out of considered to array
    #   find lowest edge and add node to considered
    #   increment total sum
    span_length = 0
    # choose random vertex and add it to set of considered points
    considered = filter(lambda x: x[0] == 1, nodes_edge)
    included_set = [1]

    while len(included_set) < 500:
        min_node = find_lowest_node(considered, included_set)
        print min_node 
        print "is min node\n"
	if min_node[0] in included_set:
	    new_node = min_node[1]
	    print new_node
	    print 'is new_node \n'
	else:
	    new_node = min_node[0]
        new_nodes = filter(lambda x: x[0] == new_node or x[1] == new_node, nodes_edge)
	considered.extend(new_nodes) # get unique nodes instead
        print considered 
        print "is considered\n"
        span_length += min_node[2]
        included_set.append(new_node)
        print str(span_length) + " is span length\n"

def find_lowest_node(nodes, included_nodes):
    print included_nodes
    print len(included_nodes)
    print 'is included nodes length\n'
    min_node = []
    for node in nodes:
        if node[0] in included_nodes and node[1] in included_nodes:
            None
	else:
	    if min_node == []:
		min_node.append(node)
	    elif node[2] < min_node[0][2]:
		min_node[0] = node
    return min_node[0]

def read_nodes_edge_file(file):
    nodes_edge = []
    with open(file, 'r') as f:
        nodes_edge = f.read().split('\n')
    f.closed
    nodes_edge = [elem.split(' ') for elem in nodes_edge][1:-1]
    return [[int(num) for num in elem] for elem in nodes_edge]

nodes_edge = read_nodes_edge_file('edges.txt')
# nodes_edge = read_nodes_edge_file('test_edge.txt')
prims_min_span_tree(nodes_edge)
