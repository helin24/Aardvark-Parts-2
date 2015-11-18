import time

def max_spacing(k, filename):
    e = EdgeHeap(filename)
    uf = UnionFind(e.node_count())

    while uf.cluster_count > k:
        length, node1, node2 = e.remove()
        # print "uniting %s and %s with distance of %s" % (node1, node2, length)
        # print uf.union(node1, node2)
        uf.union(node1, node2)

    length, node1, node2 = e.remove()
    while not uf.union(node1, node2):
        length, node1, node2 = e.remove()

    return length, node1, node2

class Node:
    def __init__(self, parent, value):
        self.parent = parent
        if parent:
            self.num_so_far = parent.get_num() + value
        else:
            self.num_so_far = ''
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_num(self):
        return self.num_so_far

    def go_to_child(self, value):
        for child in self.children:
            if child.get_num()[-1] == value:
                return child
        return False


class Trie:
    def __init__(self, filename):
        self.top_node = Node(None, None)
        f = open(filename)
        f.readline()
        count = 0
        for line in f:
            print count
            count += 1
            current_node = self.top_node
            for bit in line.split():
                # if has child with value go to that child
                # else make that child
                next_node = current_node.go_to_child(bit)
                if next_node:
                    current_node = next_node
                else:
                    current_node.add_child(Node(current_node, bit))

    def find_node(bin_str):
        current_node = self.top_node
        for bit in bin_str:
            next_node = current_node.go_to_child(bit)
            if next_node:
                current_node = next_node
            else:
                return False

        return current_node


class UnionFind:
    def __init__(self, max_node):
        self.clusters = {}
        self.cluster_count = max_node
        for node in range(1, max_node + 1):
            self.clusters[node] = [node]

    def union(self, x, y):
        x_parent, y_parent = self.find_parent(x), self.find_parent(y)
        # print "x parent and y parent are %s and %s" % (x_parent, y_parent)
        if x_parent == y_parent:
            return False
        x_count, y_count = self.count_children(x_parent), self.count_children(y_parent)
        if x_count >= y_count:
            self.clusters[x_parent].extend(self.clusters[y_parent])
            if y_count > 0:
                children = self.clusters[y_parent]
                for child_node in children:
                    self.clusters[child_node] = [x_parent]
        else:
            self.clusters[y_parent].extend(self.clusters[x_parent])
            if x_count > 0:
                children = self.clusters[x_parent]
                for child_node in children:
                    self.clusters[child_node] = [y_parent]
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

    def get_clusters(self):
        clusters = []
        for node in self.clusters.keys():
            potential_cluster = self.clusters[node]
            if potential_cluster == [node] or len(potential_cluster) > 1:
                clusters.append(sorted(potential_cluster))
        
        return clusters


class EdgeHeap:
    def __init__(self, filename):
        start = time.time()
        f = open(filename)
        self.array = []
        self.nodes_count = int(f.readline()[:-1])
        for line in f:
            node1, node2, length = (int(x) for x in line[:-1].split(' '))
            self.insert(node1, node2, length)
        print "time to make heap is %s" % (time.time() - start)

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

    

# start = time.time()
# print max_spacing(4, 'clustering1.txt')
# print time.time() - start
# 
# print max_spacing(4, 'small_cluster.txt')
# print max_spacing(3, 'linear_cluster.txt')

t = Trie('clustering_big.txt')
