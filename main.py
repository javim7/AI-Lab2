import bayesiannetworkx as bnx

bn = bnx.BayesianNetworkx()

bn.add_node("R", [], {(): [0.999, 0.001]})
bn.add_node("T", [], {(): [0.998, 0.002]})
bn.add_node("A", ["R", "T"], {(0, 0): [
    0.999, 0.001], (0, 1): [0.71, 0.29], (1, 0): [0.06, 0.94], (1, 1): [0.05, 0.95]})
bn.add_node("J", ["A"], {
    (0,): [0.95, 0.05], (1,): [0.1, 0.9]})
bn.add_node("M", ["A"], {
    (0,): [0.99, 0.01], (1,): [0.3, 0.7]})

print(bn.check_model())
print(bn.get_compact())
bn.print_factors(bn.get_factors())
bn.print_result("R", {"J": 1, "M": 1})
