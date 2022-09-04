import os

import networkx as nx
import networkx.algorithms.community

import matplotlib.pyplot as plt
import gravis as gv
from networkx.drawing.nx_agraph import graphviz_layout
from networkx.readwrite import json_graph


def plot_graph(G):


    fig = gv.vis(G, use_node_size_normalization=True,graph_height=1200,
                 node_size_normalization_max=30,
                 use_edge_size_normalization=True,
                 edge_size_data_source="0.1S",
                 edge_curvature=0.3,show_edge_label=True,
                 show_menu=False,show_details=False,details_height=0,show_details_toggle_button=False,
                 edge_label_data_source='link_type')
    fig3 = gv.d3(G, use_node_size_normalization=True,graph_height=1200,
                 node_size_normalization_max=30,
                 use_edge_size_normalization=True,
                 edge_size_data_source="0.1S",
                 edge_curvature=0.3,show_edge_label=True,
                 show_menu=False,show_details=False,details_height=0,show_details_toggle_button=False,
                use_links_force=True,
                links_force_distance=50.0,
                links_force_strength=0.5,
                 edge_label_data_source='link_type')
    fig3=gv.d3(
        data=G,
        graph_height=1000,
        details_height=100,
        show_details=True,
        show_details_toggle_button=True,
        show_menu=True,
        show_menu_toggle_button=True,
        show_node=True,
        node_size_factor=1.0,
        node_size_data_source='size',
        use_node_size_normalization=False,
        node_size_normalization_min=10.0,
        node_size_normalization_max=50.0,
        node_drag_fix=True,
        node_hover_neighborhood=True,
        node_hover_tooltip=True,
        show_node_image=True,
        node_image_size_factor=1.0,
        show_node_label=True,
        show_node_label_border=False,
        node_label_data_source='id',
        node_label_size_factor=0.8,
        node_label_rotation=0.0,
        node_label_font='Arial',
        show_edge=True,
        edge_size_factor=1.0,
        edge_size_data_source='size',
        use_edge_size_normalization=False,
        edge_size_normalization_min=0.2,
        edge_size_normalization_max=5.0,
        edge_curvature=0.3,
        edge_hover_tooltip=True,
        show_edge_label=True,
        show_edge_label_border=False,
        edge_label_data_source='link_type',
        edge_label_size_factor=1.0,
        edge_label_rotation=0.0,
        edge_label_font='Arial',
        zoom_factor=1.1,
        large_graph_threshold=500,
        layout_algorithm_active=True,

        # specific for d3
        use_many_body_force=True,
        many_body_force_strength=- 70.0,
        many_body_force_theta=0.9,
        use_many_body_force_min_distance=True,
        many_body_force_min_distance=10.0,
        use_many_body_force_max_distance=True,
        many_body_force_max_distance=1000.0,
        use_links_force=True,
        links_force_distance=50.0,
        links_force_strength=0.5,
        use_collision_force=True,
        collision_force_radius=45.0,
        collision_force_strength=0.3,
        use_x_positioning_force=True,
        x_positioning_force_strength=0.2,
        use_y_positioning_force=True,
        y_positioning_force_strength=0.5,
        use_centering_force=True,
    )
    return fig3