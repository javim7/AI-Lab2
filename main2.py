from BayesianNetwork import *

# create nodes for the network
nodes = ['A', 'B', 'C']

# create a Bayesian network with the nodes
bn = BayesianNetwork(nodes=nodes)

# add relationships between the nodes
bn.add_edge('A', 'B')
bn.add_edge('B', 'C')

# set conditional probability tables for each node
bn.set_cpt('A', {(True,): 0.9, (False,): 0.1})
bn.set_cpt('B', {(True, True): 0.8, (True, False): 0.2,
           (False, True): 0.3, (False, False): 0.7})
bn.set_cpt('C', {(True, True): 0.6, (True, False): 0.4,
           (False, True): 0.5, (False, False): 0.5})

# retrieve the conditional probability table for node B
cpt_b = bn.get_cpt('B')
print(cpt_b)
