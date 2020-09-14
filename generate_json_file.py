import sys
import json
import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
from color_selection import get_color

def read_original_file(filename):
    # Load data.json
    with open(filename, 'r') as fp:
        data_dict = json.load(fp)
        return data_dict

def process_input_data(data_dict):
    # Extract information from the read json file
    category = data_dict['category']
    nodes = data_dict['nodes']
    edges = data_dict['edges']
    num_nodes = len(nodes)
    return category, nodes, edges, num_nodes

def build_graph(n, edges):
    # Get the layout of the course map (assume the graph is a DAG)
    # n:     number of nodes
    # edges: 1D list of edges

    G = nx.DiGraph(edges)
    if not nx.is_directed_acyclic_graph(G):
        # Check if it is a DAG
        print('Warning: the given course map is not a DAG! The algorithms might fail!')
    
    # Step 1: find roots
    roots = []
    rootlevels = []
    for i in range(n):
        ancestors = nx.ancestors(G, i)
        if len(ancestors) == 0:
            roots.append(i)
            rootlevels.append(0)
    print('Roots : {}'.format(roots))
    del G

    # Step 2: calculate the layout by the Reingold-Tilford alogrithm
    g = ig.Graph(directed=True)
    g.add_vertices(n)
    g.add_edges(edges)
    layout = g.layout_reingold_tilford(mode='OUT', root=roots, rootlevel=rootlevels)
    coords = [(2 * l[0], l[1]) for l in layout]

    # === Debug ===
    G = nx.DiGraph(edges)
    coords_new = {}
    for i, (x, y) in enumerate(coords):
        coords_new[i] = (x, -y)
    nx.draw(G, coords_new)
    plt.show()
    # =============
    return coords

def process_output_data(category, nodes, edges, coords, color_type='default', cmap='rainbow'):
    # Combine information of the layout, nodes, and edges.

    # Get the color for each category
    colors = {}
    for i, c in enumerate(category):
        colors[c] = get_color(i / len(category), c_type=color_type, cmap_type=cmap)
    
    new_nodes = []
    for i, n in enumerate(nodes):
        tmp_node = {}
        tmp_node['id'] = 'n' + str(n['id'])
        tmp_node['label'] = n['label']
        tmp_node['x'] = coords[i][0]
        tmp_node['y'] = coords[i][1]
        tmp_node['size'] = 3
        tmp_node['color'] = colors[n['category']]
        tmp_node['url'] = n['url']
        tmp_node['attributes'] = { 'acategory': n['category']}
        new_nodes.append(tmp_node)
    new_edges = []
    for i, (s, t) in enumerate(edges):
        tmp_edge = {}
        tmp_edge['id'] = 'e' + str(i)
        tmp_edge['source'] = new_nodes[s]['id']
        tmp_edge['target'] = new_nodes[t]['id']
        tmp_edge['type'] = 'arrow'
        tmp_edge['size'] = 4
        new_edges.append(tmp_edge)

    new_dict = {'nodes': new_nodes, 'edges': new_edges}
    return new_dict

def write_to_json(data_dict, filename):
    # Write the results to data.json
    json_dict = json.dumps(data_dict)
    with open(filename, 'w') as fp:
        json.dump(data_dict, fp, indent=2)

if __name__ == '__main__':
    # Main function
    if len(sys.argv) != 3:
        print('Usage: python3 generate_json_file.py <course map json file> <output json file>')
        exit()
    
    input_file  = sys.argv[1] # data/course.json
    output_file = sys.argv[2] # data/data.json
    color_type  = 'cmap'      # colors for different categories: 'default'/'cmap'
    color_map   = 'rainbow'   # if color_type = 'cmap' then assign which colormap to use

    data_dict = read_original_file(input_file)
    category, nodes, edges, num_nodes = process_input_data(data_dict)
    coords = build_graph(num_nodes, edges)
    data_dict = process_output_data(
        category, nodes, edges, coords, color_type, cmap=color_map)
    write_to_json(data_dict, output_file)
