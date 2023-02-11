class BayesianNetworkx():

    # Clase representativo de una red bayesiana.
    # No toma parametros
    def __init__(self):
        self.nodes = []

    # Agrega los nodos a la red bayesiana.
    # Parametros: nombre del nodos, padres del nodo, tabla de probabilidad condicional
    def add_node(self, name, parents, cpt):
        node = {
            "name": name,
            "parents": parents,
            "cpt": cpt
        }
        self.nodes.append(node)

    # Verifica que la red bayesiana este completamente descrita.
    # Verifica que cada probabilidad de las tablas sean iguales a 1, con una tolerancia de 0.01
    # Verifica que cada probabilidad de las tablas sean iguales a la probabilidad calculada, con una tolerancia de 0.01
    # No toma parametros
    def check_model(self):
        for node in self.nodes:
            for cpt_entry in node["cpt"].values():
                if abs(cpt_entry[0] + cpt_entry[1] - 1) > 0.01:
                    return False

            for parent_states in node["cpt"].keys():
                parent_evidence = {
                    parent_name: parent_state for parent_name, parent_state in zip(node["parents"], parent_states)
                }
                cpt_prob = self.probability(node, parent_evidence)
                cpt_entry = node["cpt"][parent_states]
                if abs(cpt_entry[0] - cpt_prob[0]) > 0.01 or abs(cpt_entry[1] - cpt_prob[1]) > 0.01:
                    return False

        return True

    # Obtiene las tablas de probabilidad condicional de los nodos
    def get_cpts(self, node=None):
        if node is None:
            return [node["cpt"] for node in self.nodes]
        else:
            for n in self.nodes:
                if n["name"] == node:
                    return n["cpt"]
            raise ValueError(
                "Node '{}' not found in the Bayesian Network".format(node))

    def probability(self, node, evidence=None):
        if evidence is None:
            evidence = {}

        index = tuple(evidence[parent_name]
                      for parent_name in node["parents"])
        phi_0 = node["cpt"][index][0]
        phi_1 = node["cpt"][index][1]
        return (phi_0, phi_1)

    def printProbability(self, variable, evidence={}):
        node = next(n for n in self.nodes if n["name"] == variable)
        phi_0, phi_1 = self.probability(node, evidence)
        print("+------+----------+")
        print("| {}    |   phi({}) |".format(variable, variable))
        print("+======+==========+")
        print("| {}(0) | {:8.3f} |".format(variable, phi_0))
        print("+------+----------+")
        print("| {}(1) | {:8.3f} |".format(variable, phi_1))
        print("+------+----------+")
