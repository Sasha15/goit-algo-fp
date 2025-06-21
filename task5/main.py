import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#ADD8E6"):
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
    return graph

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb_color[0]), int(rgb_color[1]), int(rgb_color[2]))

def generate_color_gradient(start_hex, end_hex, n):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    colors = []
    for i in range(n):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (n - 1 if n > 1 else 1)
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (n - 1 if n > 1 else 1)
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (n - 1 if n > 1 else 1)
        colors.append(rgb_to_hex((r, g, b)))
    return colors

def visualize_traversal(root, traversal_func, title_prefix):
    traversal_sequence = list(traversal_func(root))
    num_nodes = len(traversal_sequence)
    
    start_color_hex = "#123456"
    end_color_hex = "#90CAF9"
    color_gradient = generate_color_gradient(start_color_hex, end_color_hex, num_nodes)

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 7))

    for i, visited_node in enumerate(traversal_sequence):
        ax.clear()
        
        tree_graph = nx.DiGraph()
        pos = {root.id: (0, 0)}
        add_edges(tree_graph, root, pos)
        
        node_colors = {}
        for j, node in enumerate(traversal_sequence[:i+1]):
            node_colors[node.id] = color_gradient[j]
        
        colors_for_drawing = [node_colors.get(node_id, data['color']) for node_id, data in tree_graph.nodes(data=True)]
        labels = {node_id: data['label'] for node_id, data in tree_graph.nodes(data=True)}
        
        ax.set_title(f"{title_prefix} - Крок {i+1}: Відвідуємо вузол {visited_node.val}", fontsize=16)
        nx.draw(tree_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors_for_drawing, ax=ax)
        plt.draw()
        plt.pause(1.5)

    plt.ioff()
    final_title = f"{title_prefix} - Завершено"
    ax.set_title(final_title, fontsize=16)
    nx.draw(tree_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors_for_drawing, ax=ax)
    plt.show()

def dfs(root):
    if not root:
        return
    stack = [root]
    visited_ids = set()
    while stack:
        node = stack.pop()
        if node.id not in visited_ids:
            yield node
            visited_ids.add(node.id)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs(root):
    if not root:
        return
    queue = deque([root])
    visited_ids = set()
    while queue:
        node = queue.popleft()
        if node.id not in visited_ids:
            yield node
            visited_ids.add(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.left = Node(3)
    root.right.right = Node(2)

    print("Починається візуалізація обходу в глибину (DFS)...")
    visualize_traversal(root, dfs, "Обхід в глибину (DFS)")

    print("\nПочинається візуалізація обходу в ширину (BFS)...")
    visualize_traversal(root, bfs, "Обхід в ширину (BFS)")
