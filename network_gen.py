
import networkx as nx

def add_color(G, nodes, edges):
    colors = ['darkgreen', 'blue', 'darkgreen', 'darkred', 'pink']
    for node in nodes:
        if G.nodes[node]['node_type'] == "PLANT":
            G.nodes[node]['color'] = colors[1]
            G.nodes[node]['shape'] = "circle"
            G.nodes[node]['size'] = 10
        elif G.nodes[node]['node_type'] == "RSV":
            G.nodes[node]['color'] = colors[3]
            G.nodes[node]['shape'] = "rectangle"
            G.nodes[node]['size'] = 10
        else:
            G.nodes[node]['color'] = colors[2]
            G.nodes[node]['shape'] = "triangle"
            G.nodes[node]['size'] = 10
    for edge in edges:
        if G.edges[edge[0],edge[1]]['link_type']=="WaterOut":
            G.edges[edge[0],edge[1]]['color'] = "blue"
        else:
            G.edges[edge[0],edge[1]]['color'] = "red"

def generate_network(parser):
    G = nx.DiGraph()
    for n in parser.plants():
        G.add_node(n, type="PLANT")
        nx.set_node_attributes(G, {n:"PLANT"}, "node_type")
        nx.set_node_attributes(G, {n:n}, "node_name")
    for n in parser.rsrv():
        G.add_node(n, type="RSV")
        nx.set_node_attributes(G, {n:"RSV"}, "node_type")
        nx.set_node_attributes(G, {n:n}, "node_name")
    for n in parser.wtrw():
        G.add_node(n, type="WTR")
        nx.set_node_attributes(G, {n:"WTR"}, "node_type")
        nx.set_node_attributes(G, {n:n}, "node_name")
    for n in parser.wtr_out():
        G.add_edge(n[0], n[1])
        attrs={(n[0], n[1]):{"link_type": "WaterOut"}}
        nx.set_edge_attributes(G, attrs)
    for n in parser.flood_route_out():
        G.add_edge(n[0], n[1])
        attrs={(n[0], n[1]):{"link_type": "FloodroutOut" }}
        nx.set_edge_attributes(G, attrs)
    all_nodes= [x for x, y in G.nodes(data=True)if y['node_type'] != None]
    all_edges = [x for x in G.edges(data=True) ]
    return G, all_nodes, all_edges