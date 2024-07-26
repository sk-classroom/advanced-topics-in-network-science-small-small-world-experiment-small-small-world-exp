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

assert isinstance(gs, igraph.Graph), f"Expected the returned value to be of type igraph.Graph, got {type(gs)}"
assert gs.vcount() == 63333, f"Expected 63333 nodes in the largest connected component, got {gs.vcount()}"

print("Testing get_largest_connected_component (airport network) ...")
g = load_airport_net()
gs = get_largest_connected_component(g)
assert gs.vcount() == 2905, f"Expected 2905 nodes in the largest connected component, got {gs.vcount()}"
