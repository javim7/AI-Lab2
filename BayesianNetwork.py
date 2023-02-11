class BayesianNetwork:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or {}
        self.CPT = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, parent, child):
        if parent not in self.edges:
            self.edges[parent] = []
        self.edges[parent].append(child)

    def set_cpt(self, node, cpt):
        self.CPT[node] = cpt

    def get_cpt(self, node):
        return self.CPT.get(node, None)
