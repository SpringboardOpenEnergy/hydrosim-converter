import lxml.etree as etree
import codecs
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx

class SimModelParser:
    def __init__(self):
        self.__plants = {}
        self.__rsrv = {}
        self.__wtrw = {}
        self.__wtr_out = []
        self.__floodroute_out = []

    def parser_name(self):
        return "v1"

    def plants(self):
        return self.__plants.keys()
    def rsrv(self):
        return self.__rsrv.keys()
    def wtrw(self):
        return self.__wtrw.keys()
    def flood_route_out(self):
        return self.__floodroute_out
    def wtr_out(self):
        return self.__wtr_out

    def add_link(self, elem, list):
        x = elem.findall("./from")[0].text
        y = elem.findall("./to")[0].text
        list.append((x,y))

    def parse_xml(self, file_name):
        xmlt=codecs.open(file_name,"r",encoding='ISO-8859-1').read()
        root = etree.XML(xmlt.encode("ISO-8859-1"))
        for el in root.findall(".//*/simobject"):
            tp=el.attrib['type']
            for elem in el.getchildren():
                if elem.tag=="name":
                    if tp=="RSV":
                        if elem.text not in self.__rsrv:
                            self.__rsrv[elem.text]=elem.text
                    if tp=="PLANT":
                        if elem.text not in self.__plants:
                            self.__plants[elem.text]=elem.text
                    if tp=="WTR":
                        if elem.text not in self.__wtrw:
                            self.__wtrw[elem.text]=elem.text

        for el in root.findall(".//*/Connections"):
            for elem in el.getchildren():
                if elem.tag=="wtr_out":
                    self.add_link(elem, self.__wtr_out)
                if elem.tag=="floodroute_out":
                    self.add_link(elem, self.__floodroute_out)
