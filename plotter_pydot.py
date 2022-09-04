import networkx as nx

def plot_graph(G, fname):
    pdot = nx.drawing.nx_pydot.to_pydot(G)
    shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star', ]
    colors = ['blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b']
    styles = ['filled', 'rounded', 'rounded, filled', 'dashed', 'dotted, bold']
    mainshape = 'box'
    maincol = 'black'
    mainstyle = 'rounded, bold'
    for i, node in enumerate(pdot.get_nodes()):
        node.set_label(node.get_name())
        # print(node.get_name())
        node.set_shape(mainshape)  # shapes[random.randrange(len(shapes))])
        node.set_fontcolor('gray')  # colors[random.randrange(len(colors))])
        # node.set_fillcolor(colors[random.randrange(len(colors))])
        node.set_style(mainstyle)  # styles[random.randrange(len(styles))])
        # node.set_color(colors[random.randrange(len(colors))])

    for i, edge in enumerate(pdot.get_edges()):
        #edge.set_label(float(edge.get('percentage')))
        # print(edge.get('percentage'))
        edge.set_fontcolor('black')  # (colors[random.randrange(len(colors))])
        # edge.set_style(styles[random.randrange(len(styles))])
        edge.set_color('dakgeen')  # colors[random.randrange(len(colors))])
    pdot.write_png(fname)

