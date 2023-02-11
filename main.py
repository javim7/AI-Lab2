from BayesianNetworkx import *


bn = BayesianNetworkx()

bn.add_node("R", [], {(): [0.999, 0.001]})
bn.add_node("T", [], {(): [0.998, 0.002]})
bn.add_node("A", ["R", "T"], {(0, 0): [
    0.999, 0.001], (0, 1): [0.71, 0.29], (1, 0): [0.06, 0.94], (1, 1): [0.05, 0.95]})
bn.add_node("J", ["A"], {
    (0,): [0.95, 0.05], (1,): [0.1, 0.9]})
bn.add_node("M", ["A"], {
    (0,): [0.99, 0.01], (1,): [0.3, 0.7]})

print(bn.check_model())
print(bn.get_cpts())
# calculando probablidades de prueba
# pR = bn.printProbability("R", {})
# print("")
# pT = bn.printProbability("T", {})

# evidence = {"R": 0, "T": 0}
# pA = bn.printProbability("A", evidence)
# # print("Probabilidad de  A:", pA)

# evidence2 = {"R": 0, "T": 0, "A": 1}
# pJ = bn.printProbability("J", evidence2)
# pM = bn.printProbability("M", evidence2)
