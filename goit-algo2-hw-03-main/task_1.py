import networkx as nx


def build_graph():
    G = nx.DiGraph()

    edges = [
        ('Термінал1', 'Склад1', 25), ('Термінал1',
                                      'Склад2', 20), ('Термінал1', 'Склад3', 15),
        ('Термінал2', 'Склад3', 15), ('Термінал2',
                                      'Склад4', 30), ('Термінал2', 'Склад2', 10),
        ('Склад1', 'Магазин1', 15), ('Склад1',
                                     'Магазин2', 10), ('Склад1', 'Магазин3', 20),
        ('Склад2', 'Магазин4', 15), ('Склад2',
                                     'Магазин5', 10), ('Склад2', 'Магазин6', 25),
        ('Склад3', 'Магазин7', 20), ('Склад3',
                                     'Магазин8', 15), ('Склад3', 'Магазин9', 10),
        ('Склад4', 'Магазин10', 20), ('Склад4',
                                      'Магазин11', 10), ('Склад4', 'Магазин12', 15),
        ('Склад4', 'Магазин13', 5), ('Склад4', 'Магазин14', 10)
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)

    return G


def max_flow(G, source):
    total_flow = 0
    flow_results = []

    for sink in [f'Магазин{i}' for i in range(1, 15)]:
        flow_value, flow_dict = nx.maximum_flow(G, source, sink)
        total_flow += flow_value

        for warehouse in G.successors(source):
            if flow_dict.get(warehouse, {}).get(sink, 0) > 0:
                flow_results.append((source, sink, flow_dict[warehouse][sink]))

    return total_flow, flow_results


def main():
    G = build_graph()

    total_flow_T1, flow_results_T1 = max_flow(G, 'Термінал1')
    total_flow_T2, flow_results_T2 = max_flow(G, 'Термінал2')

    print("Максимальний потік:", total_flow_T1 + total_flow_T2)

    for terminal, store, flow in flow_results_T1 + flow_results_T2:
        print(f"{terminal} {store} {flow}")


if __name__ == "__main__":
    main()
