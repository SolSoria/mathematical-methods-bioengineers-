import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters for the Erdős-Rényi graph
N = 1000  # Number of nodes
p = 0.01  # Probability of edge creation

# Generate the Erdős-Rényi graph
G = nx.erdos_renyi_graph(N, p)

# Calculate the degree of each node
degrees = [deg for _, deg in G.degree()]

# Compute the degree distribution
degree_counts = np.bincount(degrees)
degree_probabilities = degree_counts / sum(degree_counts)

# Plot p(k) versus k
plt.figure(figsize=(10, 6))
plt.scatter(range(len(degree_probabilities)), degree_probabilities, alpha=0.7)
plt.title("Degree Distribution p(k) vs. k for Erdős-Rényi Network (N=1000, p=0.01)")
plt.xlabel("Degree (k)")
plt.ylabel("Probability p(k)")
plt.yscale("log")  # Optional: log scale for better visibility
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
