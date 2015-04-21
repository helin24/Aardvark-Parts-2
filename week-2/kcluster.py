def kcluster(nodes_edge, num_clusters):
	print nodes_edge 

def read_nodes_edge_file(file):
	nodes_edge = []
	with open(file, 'r') as f:
		nodes_edge = f.read().split('\n')
	f.closed
	nodes_edge = [elem.split(' ') for elem in nodes_edge][1:-1]
	return [[int(num) for num in elem] for elem in nodes_edge]

nodes_edge = read_nodes_edge_file('test.txt')
kcluster(nodes_edge, 1)
