import networkx as nx
import matplotlib.pyplot as plt

# Take input
n = int(input("Enter number of vertices: "))

# Create complete graph
G = nx.complete_graph(n)

# Relabel nodes from 0..n-1 to 1..n
G = nx.relabel_nodes(G, {i: i+1 for i in range(n)})

# Print vertices
print("\nVertices:")
print(list(G.nodes()))

# Print edges
print("\nEdges:")
for edge in G.edges():
    print(edge)

print("\nTotal number of edges:", G.number_of_edges())

# Draw graph
plt.figure(figsize=(6, 6))
pos = nx.circular_layout(G)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="#4A90E2",
    node_size=800,
    font_size=12,
    font_weight="bold",
    edge_color="gray"
)

plt.title("Complete Graph", fontsize=14, fontweight="bold")
plt.show()