import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_tree(tree_root, title=""):
    if tree_root is None:
        print("Дерево порожнє.")
        return
        
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap_array, i=0):
    if i >= len(heap_array):
        return None
    
    node = Node(heap_array[i])
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    
    node.left = heap_to_tree(heap_array, left_child_index)
    node.right = heap_to_tree(heap_array, right_child_index)
    
    return node


if __name__ == '__main__':
    heap_array_from_image = [0, 4, 1, 5, 10, 3]
    tree_root_from_image = heap_to_tree(heap_array_from_image)
    draw_tree(tree_root_from_image, "Візуалізація дерева з масиву (відповідає зображенню)")
    
    raw_data = [3, 5, 1, 6, 2, 8, 0, 9, 4, 7]
    heapq.heapify(raw_data)
    
    heap_root = heap_to_tree(raw_data)
    draw_tree(heap_root, "Візуалізація бінарної купи (min-heap)") 