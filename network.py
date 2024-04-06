import random
from bayesian_node import *
# Ora puoi utilizzare le funzioni e le classi definite in node.py

from typing import List

class Network:
    def __init__(self, nodes:List[BayesianNode]):
        self.net_nodes = nodes

    def topological_sort(self):
        visited = []
        parents_count = {node: 0 for node in self.net_nodes}

        # InizializzO il conteggio dei genitori per ciascun nodo
        for node in self.net_nodes:
            for child in node.children:
                parents_count[child] += 1

        # TrovO nodi senza genitori
        no_parents = [node for node in self.net_nodes if parents_count[node] == 0]

        # IterO sui nodi senza genitori e visita i loro figli
        while no_parents:
            node = no_parents.pop(0)
            visited.append(node)
            for child in node.children:
                parents_count[child] -= 1
                if parents_count[child] == 0:
                    no_parents.append(child)

        return visited
