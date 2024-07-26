# %% Import
from scipy import sparse
import pandas as pd
import igraph
import numpy as np

# %% Define functions

def to_igraph(src, trg):
    g = igraph.Graph.TupleList(list(zip(src, trg)), directed=False)
    return g

def load_airport_net():
    edge_table = pd.read_csv(
        "https://raw.githubusercontent.com/skojaku/core-periphery-detection/master/data/edge-table-airport.csv"
    )
    src, trg = edge_table["source"], edge_table["target"]
    g = to_igraph(src, trg)
    return g


# %% Test get_largest_connected_component
print("Testing get_largest_connected_component ...")

edge_table = pd.read_csv("./data/edge_coauthorship.csv")
src, trg = edge_table["src"], edge_table["trg"]
g = to_igraph(src, trg)
gs = get_largest_connected_component(g)
ave_path = get_average_path_length(gs)

assert isinstance(ave_path, float), f"Expected the returned value to be of type float, got {type(ave_path)}"
assert 3.9 < ave_path < 4.3, f"Expected average path length is between 3.9 and 4.3, got {ave_path}"

print("Testing get_largest_connected_component (airport network) ...")
g = load_airport_net()
gs = get_largest_connected_component(g)
ave_path = get_average_path_length(gs)
assert isinstance(ave_path, float), f"Expected the returned value to be of type float, got {type(ave_path)}"
assert 3.9 < ave_path < 4.3, f"Expected average path length is between 3.9 and 4.3, got {ave_path}"