from pulp import *

class BipartiteGraph:
    def __init__(self):

        self.employees = set()
        self.beers = set()
        self.adj_list = {}

    def add_vertex(self, vertex, set_type):

        if set_type == 'employees':
            self.employees.add(vertex)
        elif set_type == 'beers':
            self.beers.add(vertex)
        else:
            raise ValueError("set_type must be either 'employees' or 'beers'")
        self.adj_list[vertex] = []

    def add_edge(self, u, v):

        if (u in self.employees and v in self.beers) or (u in self.beers and v in self.employees):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            raise ValueError("Edge must connect vertices from different sets")

    def is_bipartite(self):

        color = {}
        for vertex in list(self.employees) + list(self.beers):
            if vertex not in color:
                if not self._bfs_check(vertex, color):
                    return False
        return True

    def _bfs_check(self, start, color):

        from collections import deque
        queue = deque([start])
        color[start] = 0

        while queue:
            vertex = queue.popleft()
            current_color = color[vertex]

            for neighbor in self.adj_list[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False

        return True

    sorts = [set() for _ in range(b)]
    def solve_ilp_set_cover(sorts, n):


    def display(self):
        print("Set employees:", self.employees)
        print("Set beers:", self.beers)
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")



# Example usage:
graph = BipartiteGraph()
graph.add_vertex('A', 'beers')
graph.add_vertex('B', 'beers')
graph.add_vertex('1', 'employees')
graph.add_vertex('2', 'employees')

graph.add_edge('A', '1')
graph.add_edge('A', '2')
graph.add_edge('B', '1')

graph.display()

if graph.is_bipartite():
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
