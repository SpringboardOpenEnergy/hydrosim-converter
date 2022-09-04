import lxml.etree as etree
import codecs
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import networkx as nx

class SimModelParser:
    def __init__(self):
        self.__plants = {}
        self.__rsrv = {}
        self.__links = {}
        self.__wtrw = {}
        self.__wtr_out = []
        self.__floodroute_out = []

    def parser_name(self):
        return "v2"

    def parse_link(self, elem, list):
        mp = {}
        sequence = []
        def check_add(name):
            if name not in mp:
                mp[name] = name
                sequence.append(name)
        def split_ckeck(name):
            cols = name.split("_")
            for i in range(1, len(cols)):
                check_add(cols[i])
        x = elem.findall("./from")[0].text
        y = elem.findall("./to")[0].text
        split_ckeck(x)
        split_ckeck(y)
        if len(sequence) == 2:
            txt=str(sequence[0] + sequence[1])
            if txt not in self.__links:
                list.append((sequence[0], sequence[1]))
                self.__links[txt]=txt
        else:
            txt = str(sequence[0] + sequence[1])
            if txt not in self.__links:
                list.append((sequence[0], sequence[1]))
                self.__links[txt] = txt
            txt = str(sequence[1] + sequence[2])
            if txt not in self.__links:
                list.append((sequence[1], sequence[2]))
                self.__links[txt] = txt

    def check_wtrway_name(self, name):
        cols=name.split("_")   #Names in XML contain both source node and waterway
        for i in range(1,len(cols)):
            if cols[i] not in self.__plants and cols[i] not in self.__rsrv:
                self.__wtrw[cols[i]]=cols[i]

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

        # Second parse, to make sure the WTR objects are not already assigned
        for el in root.findall(".//*/simobject"):
            tp = el.attrib['type']
            for elem in el.getchildren():
                if elem.tag == "name":
                    if tp == "WTR":
                        self.check_wtrway_name(elem.text)


        for el in root.findall(".//*/Connections"):
            for elem in el.getchildren():
                if elem.tag=="wtr_out":
                    self.parse_link(elem, self.__wtr_out)
                if elem.tag=="floodroute_out":
                    self.parse_link(elem, self.__floodroute_out)

