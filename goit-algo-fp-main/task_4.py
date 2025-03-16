import uuid
import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_heap_edges(graph, heap_nodes, pos, i=0, x=0, y=0, layer=1):

    if i < len(heap_nodes):
        node = heap_nodes[i]
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)

        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(heap_nodes):
            graph.add_edge(node.id, heap_nodes[left_idx].id)
            add_heap_edges(graph, heap_nodes, pos, left_idx,
                           x - 1 / 2 ** layer, y - 1, layer + 1)

        if right_idx < len(heap_nodes):
            graph.add_edge(node.id, heap_nodes[right_idx].id)
            add_heap_edges(graph, heap_nodes, pos, right_idx,
                           x + 1 / 2 ** layer, y - 1, layer + 1)

    return graph


def draw_heap(heap):
    heap_nodes = [HeapNode(val) for val in heap]
    tree = nx.DiGraph()
    pos = {}

    tree = add_heap_edges(tree, heap_nodes, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


heap = [10, 8, 9, 7, 6, 5, 4, 3, 2, 1]
draw_heap(heap)
