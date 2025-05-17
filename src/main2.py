from functools import cmp_to_key
import csv
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
def comparator(a, b):
    return a[2] - b[2]


def kruskals_mst(V, edges):
    edges = sorted(edges, key=cmp_to_key(comparator))
    dsu = DSU(V)
    cost = 0
    count = 0
    mst_edges = []
    for x, y, w in edges:
        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            count += 1
            mst_edges.append((x, y, w))
            if count == V - 1:
                break
    return cost, mst_edges


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1

def parse():
    df = pd.read_csv('communication_wells.csv')
    df.head()
    G2 = nx.DiGraph()
    G2 = nx.from_pandas_edgelist(df, source='start_well', target='finish_well', edge_attr='distance')
    G2.nodes()
    pos = nx.spring_layout(G2)
    weights = list(nx.get_edge_attributes(G2, 'distance').values())
    weights = [i / 500 for i in weights]
    nx.draw_networkx_nodes(G2, pos, node_size=800, alpha=0.5)
    nx.draw_networkx_edges(G2, pos, width=weights)
    nx.draw_networkx_labels(G2, pos)
    plt.show()

if __name__ == '__main__':
    parse()
    with open('communication_wells.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        id_well = {}
        id_next = 0
        edges = []
        min_weight_edges = {}
        def clean_name(name):
            name = name.strip()
            name = name.replace('К', 'K')
            return name

        for row in csv_reader:
            start_well, finish_well, distance = row
            start_well = clean_name(start_well)
            finish_well = clean_name(finish_well)

            if start_well not in id_well:
                id_well[start_well] = id_next
                id_next += 1

            if finish_well not in id_well:
                id_well[finish_well] = id_next
                id_next += 1

            key = tuple(sorted([start_well, finish_well]))
            if key not in min_weight_edges or distance < min_weight_edges[key][2]:
                min_weight_edges[key] = (start_well, finish_well, distance)

        for (start_well, finish_well, distance) in min_weight_edges.values():
            edges.append((id_well[start_well], id_well[finish_well], int(distance)))


        res = kruskals_mst(len(id_well), edges)

        id_to_well = {x: y for y, x in id_well.items()}
        mst_named_edges = []
        for x, y, w in res[1]:
            u = id_to_well[x]
            v = id_to_well[y]
            mst_named_edges.append((u, v, w))
        df_mst = pd.DataFrame(mst_named_edges, columns=['start_well', 'finish_well', 'distance'])
        G_mst = nx.Graph()
        G_mst = nx.from_pandas_edgelist(df_mst, source='start_well', target='finish_well', edge_attr='distance')
        G_mst.nodes()
        pos = nx.spring_layout(G_mst)
        weights = list(nx.get_edge_attributes(G_mst, 'distance').values())
        weights = [i / 500 for i in weights]
        nx.draw_networkx_nodes(G_mst, pos, node_size=800, alpha=0.5)
        nx.draw_networkx_edges(G_mst, pos, width=weights)
        nx.draw_networkx_labels(G_mst, pos)
        plt.show()

        if len(edges) < len(id_well) - 1:
            print(-1)
        else:
            print(res)
