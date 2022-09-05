
from plain_parser import SimModelParser
from resolver_parser import SimModelParser as SimModelParser2
from network_gen import generate_network, add_color
from plotter_d3 import plot_graph
from plotter_pydot import plot_graph as pyplot_graph
from rdf_gen import rdf_gen
import os, codecs



def process_input(file, parser):
    parser.parse_xml(file)  #Parses the file and populates plants, wrtr, rsrv lists with names of nodes
    G, all_nodes, all_edges=generate_network(parser)  #Generates a networkx graph based on the parsed lists
    add_color(G, all_nodes, all_edges)  #Adds color codes
    pyplot_graph(G, './pyplot_' + parser.parser_name() + '.png')  #Exports to PNG file
    fig=plot_graph(G)
    fname='./d3_' + parser.parser_name() + '.html'   #Exports to D3
    html=fig.to_html()
    file = codecs.open(fname, "w", "utf-8")
    file.write(str(html))
    file.close()
    rdf_gen(G, all_nodes, all_edges, './rdf_' + parser.parser_name() + '.txt')

if __name__ == '__main__':
    # 2 different parsers. One includes all watercourses as given in the XML - some of which duplicates links
    # the other combines information to reduce number of nodes
    parser=SimModelParser()
    process_input("./hydsimexport.xml", parser)
    parser=SimModelParser2()
    process_input("./hydsimexport.xml", parser)
