# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

from graph import Base,Node,Edge,EdgeWeighted

##from graph_single import *
##from graph_concrete import *
##from graph_join import *

if __name__ == "__main__" :
## connection to local SQLite database
##    engine = create_engine("sqlite://dbname")
    engine = create_engine("sqlite:///graph.db")
## connection to postgreSQL database (via ENIB tempo server)
##    engine = create_engine('postgres://username:password@tempo/dbname')
##    engine = create_engine('postgres://msi_b24@tempo/msi_db24')
    session = sessionmaker(engine)()
    print("------------------- edges ----------------------")
    edges=session.query(EdgeWeighted).all()
    for edge in edges :
        print(edge ,"  ------> weight : ",edge.get_weight() )
        # TO DO :
        #  -- afficher le premier noeud (above) de chaque arete
        node = edge.get_node_above()
        print("node above :", node.get_name())
        #  -- afficher les aretes qui partent de ce noeud (following)
        for ed in node.following_edgesweighted:
            print("following edges :", ed)
        #  -- afficher le deuxieme noeud (below) de chaque arete
        nodeB = edge.get_node_below()
        print("node below :", nodeB.get_name())

        #  -- afficher les aretes qui arrivent sur ce noeud (previous)
        for ed in nodeB.previous_edgesweighted:
            print("previous edges :", ed)



    print("------------------- nodes ----------------------")
    nodes=session.query(Node).all()
    for node in nodes :
        print(node)
        # TO DO :
        #  -- afficher le noeud (above)
        print("Node:",node.get_name())
        #  -- afficher le nombre de noeuds qui le précède (above_neighbors())
        cpt=0
        for abv in node.above_neighbors() :
            cpt = cpt +1

        print("total of  neighbors above : ", cpt)

        #  -- afficher les noeuds  qui le précède (above)
        for above in node.above_neighbors() : 
            print(" neighbors above : ",above.get_name())

        #  -- afficher le nombre de noeuds qui le suivent  (below_neighbors())
        cpt=0
        for blw in node.below_neighbors() :
            cpt = cpt +1

        print("total of neighbors below : ", cpt)        
       
        #  -- afficher les noeuds  qui le précède (below)
        for below in node.below_neighbors():
            print("neighbors below : ",below.get_name())
  

## look at the relational database :
##{logname@hostname}sqlite3 graph.db
##sqlite> .headers on
##sqlite> .mode column
##sqlite> .width 10
##sqlite> .tables
##select * from edges;
##sqlite> select * from nodes;
