def max_spacing(k, filename):
    e = EdgeHeap(filename)
    uf = UnionFind(e.node_count())
    print uf.cluster_count

    while uf.cluster_count > k:
        length, node1, node2 = e.remove()
        print "uniting %s and %s" % (node1, node2)
        print uf.union(node1, node2)

    print e.show_array()

    # {1: 1 or 1 points to [1, 2, 3] and then 2:1 3:1} so then can search what pointer a node has (or is itself)


class UnionFind:
    def __init__(self, max_node):
        self.clusters = {}
        self.cluster_count = max_node
        for node in range(1, max_node + 1):
            self.clusters[node] = [node]

    def union(self, x, y):
        x_parent, y_parent = self.find_parent(x), self.find_parent(y)
        print "x parent and y parent are %s and %s" % (x_parent, y_parent)
        if x_parent == y_parent:
            return False
        x_count, y_count = self.count_children(x), self.count_children(y)
        if x_count >= y_count:
            self.clusters[x].extend(self.clusters[y])
            if y_count > 0:
                children = self.clusters[y]
                for child_node in children:
                    self.clusters[child_node] = [x]
        else:
            self.clusters[y].extend(self.clusters[x])
            if x_count > 0:
                children = self.clusters[x]
                for child_node in children:
                    self.clusters[child_node] = [y]
        self.cluster_count -= 1
        return True
        
    def find_parent(self, node):
        parent_or_children = self.clusters[node]
        if len(parent_or_children) == 1:
            return parent_or_children[0]
        else:
            return node

    def count_children(self, node):
        parent_or_children = self.clusters[node]
        if len(parent_or_children) == 0:
            return 0
        else:
            return len(parent_or_children)


    # open file
    # make heap of edges based on their length (smallest to top)
        # edge length


class EdgeHeap:
    def __init__(self, filename):
        f = open(filename)
        self.array = []
        self.nodes_count = int(f.readline()[:-1])
        for line in f:
            node1, node2, length = (int(x) for x in line[:-1].split(' '))
            self.insert(node1, node2, length)

    def show_array(self):
        return self.array[:50]

    def node_count(self):
        return self.nodes_count

    def insert(self, node1, node2, length):
        self.array.append((length, node1, node2))
        current_index = len(self.array) - 1
        parent_index = self.parent_index(current_index)
        while parent_index is not None and self.array[parent_index][0] > length:
            self.swap(parent_index, current_index)
            current_index = parent_index
            parent_index = self.parent_index(parent_index)

    def remove(self):
        top_node = self.array[0]
        new_value = self.array.pop()
        self.array[0] = new_value
        current_index = 0
        left_index, right_index = self.child_indices(current_index)
        
        while left_index:
            swap_index = None
            if self.array[left_index] < new_value:
                swap_index = left_index
            if right_index and self.array[right_index] < new_value and self.array[right_index] < self.array[left_index]:
                swap_index = right_index

            if swap_index:
                self.swap(current_index, swap_index)
                current_index = swap_index
                left_index, right_index = self.child_indices(current_index)
            else:
                break

        return top_node
        

    def parent_index(self, index):
        p = (index - 1) / 2
        if p >= 0:
            return p

    def child_indices(self, index):
        if 2 * (index + 1) < len(self.array):
            return 2 * index + 1, 2 * (index + 1)
        elif 2 * index + 1 < len(self.array):
            return 2 * index + 1, None
        else:
            return None, None

    def swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

    


max_spacing(4, 'clustering1.txt')

