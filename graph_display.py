# -*- coding: utf-8 -*-
import os
os.environ["PATH"] += os.pathsep + 'D:\Graphviz\release\bin'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pydot
from graph import Base,Node,Edge

## from graph_single import *
## from graph_concrete import *
## from graph_join import *

if __name__ == "__main__" :
## connection to local SQLite database
##    engine = create_engine("sqlite://dbname")
    engine = create_engine("sqlite:///graph.db")
## connection to postgreSQL database (via ENIB tempo server)
##    engine = create_engine('postgres://username:password@tempo/dbname')
##    engine = create_engine('postgres://msi_b24@tempo/msi_db24')
    session = sessionmaker(engine)()
    # TODO : rechercher les noeuds et aretes dans la base graph.db
    # TODO : visualiser le graphe
    graph = pydot.Dot(graph_type='digraph')
    n1,n2="Brest","Quimper"
    c1,c2,weight="red","green",70
    dot_n1 = pydot.Node(n1, style="filled", fillcolor=c1)
    dot_n2 = pydot.Node(n2, style="filled", fillcolor=c2)
    dot_edge=pydot.Edge(dot_n1,dot_n2,label=weight)
    graph.add_node(dot_n1)
    graph.add_node(dot_n2)
    graph.add_edge(dot_edge)
    graph.write_png('bretagne-1.png')
