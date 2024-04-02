import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Pool
import pandas as pd

# Load data from people.csv
people_data = pd.read_csv('Datasets/dataset1/people.csv')

# Filter relevant nodes and edges
# Example: Filter nodes based on affiliation_name
relevant_people = people_data[people_data['affiliation_name'].notnull()]

# Create a graph using relevant nodes and edges
startup_network = nx.Graph()

# Add nodes to the graph
for index, person in relevant_people.iterrows():
    startup_network.add_node(person['object_id'], **person)

# Add edges to the graph based on relationships between individuals
# Example: If two individuals worked together at the same company, add an edge between them
# You may need additional data to establish relationships between individuals

# Define a function to visualize the graph
def visualize_graph(graph):
    # Customize visualization settings to optimize performance
    # Example: Reduce node size, limit the number of displayed nodes, use a simpler layout algorithm
    options = {
        'node_size': 10,
        'width': 0.1,
        # Add more visualization options as needed
    }
    nx.draw(graph, **options)
    plt.savefig('startup_network.png')  # Save visualization as .png file

# Use parallel processing to speed up graph construction if needed
def construct_graph_parallel(data_chunk):
    graph_chunk = nx.Graph()
    # Construct a portion of the graph using the given data chunk
    # Add nodes and edges to the graph
    return graph_chunk

if __name__ == '__main__':
    # Split data into chunks for parallel processing
    # Example: If using multiprocessing, split the data into chunks and process each chunk in parallel
    # You may need to adjust the chunk size based on the available resources and the size of your data

    # Create a pool of worker processes
    pool = Pool()

    # Process data chunks in parallel and merge the results
    # Example: Use pool.map() to apply the construct_graph_parallel function to each data chunk
    # You may need to merge the resulting graphs into a single graph

    # Visualize the final graph
    visualize_graph(startup_network)
