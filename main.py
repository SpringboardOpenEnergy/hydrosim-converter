
from plain_parser import SimModelParser
from resolver_parser import SimModelParser as SimModelParser2
from network_gen import generate_network, add_color
from plotter_d3 import plot_graph
from plotter_pydot import plot_graph as pyplot_graph
from rdf_gen import rdf_gen
import os
def process_input(file, parser):
    parser.parse_xml(file)
    G, all_nodes, all_edges=generate_network(parser)
    add_color(G, all_nodes, all_edges)
    pyplot_graph(G, './pyplot_' + parser.parser_name() + '.png')
    fig=plot_graph(G)
    fname='./d3_' + parser.parser_name() + '.html'
    try:
        os.remove(fname)
    except:
        pass
    fig.export_html(fname)
    rdf_gen(G, all_nodes, all_edges, './rdf_' + parser.parser_name() + '.txt')

if __name__ == '__main__':
    parser=SimModelParser()
    process_input("./Begna.basic.xml", parser)
    parser=SimModelParser2()
    process_input("./Begna.basic.xml", parser)
