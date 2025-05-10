from functools import cmp_to_key
import csv

def comparator(a, b):
    return a[2] - b[2];


def kruskals_mst(V, edges):
    edges = sorted(edges, key=cmp_to_key(comparator))

    dsu = DSU(V)
    cost = 0
    count = 0
    for x, y, w in edges:

        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)
            cost += w
            count += 1
            if count == V - 1:
                break
    return cost


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


if __name__ == '__main__':
    with open('communication_wells.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        id_well = {}
        id_next = 0
        edges = []
        for row in csv_reader:
            start_well, finish_well, distance = row
            if start_well not in id_well:
                id_well[start_well] = id_next
                id_next += 1
            if finish_well not in id_well:
                id_well[finish_well] = id_next
                id_next += 1
            edges.append((id_well[start_well], id_well[finish_well], int(distance)))

        res = kruskals_mst(len(id_well), edges)
        if len(edges) < len(id_well) - 1:
            print(-1)
        else:
            print(res)
