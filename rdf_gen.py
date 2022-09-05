from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD
from rdflib import Namespace


def rdf_gen(G, all_nodes, all_edges, output_file):
    node_map={}
    # Create an RDF Graph  (to be based on the input Networkx graph
    g = Graph()  #
    dbo = Namespace("http://dbpedia.org/ontology/")
    plant = dbo.PowerStation
    rsrv = dbo.Reservoir
    wtr = dbo.WaterCourse

    for node in all_nodes:
        n = URIRef("http://example.org/" + G.nodes[node]['node_name'])
        node_map[G.nodes[node]['node_name']] = n  #Cache for when setting edges
        if G.nodes[node]['node_type']=="PLANT":
            g.add((n, RDF.type, plant))
        if G.nodes[node]['node_type']=="RSV":
            g.add((n, RDF.type, rsrv))
        if G.nodes[node]['node_type']=="WTR":
            g.add((n, RDF.type, wtr))
        g.add((n, FOAF.name, Literal(G.nodes[node]['node_name'])))

    link_water_out = dbo.WaterOut# URIRef("http://example.org/WATER_OUT")
    g.add((link_water_out, FOAF.name, Literal("Water Out")))
    link_floodrout_out = dbo.FloodRouteOut # URIRef("http://example.org/FLOOD_ROUTE_OUT")
    g.add((link_floodrout_out, FOAF.name, Literal("Flood Route Out")))
    for edge in all_edges:
        if G.edges[edge[0], edge[1]]['link_type'] == "WaterOut":
            #Lookup RDF subject/object from node_map via name. Then set predicate
            g.add((node_map[edge[0]], link_water_out, node_map[edge[1]]))
        else:
            g.add((node_map[edge[0]], link_floodrout_out, node_map[edge[1]]))

    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))
    g.serialize(destination=output_file, format='turtle')