from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    # TODO create and save a graph
    Brest = Node("Brest")
    Quimper = Node("Quimper")
    Saintb = Node("saint-brieuc")
    Vannes = Node("Vannes")
    Rennes = Node ("Rennes")
    Nantes = Node ("Nantes")

    edge=EdgeWeighted(Brest,Quimper,10)
    edge2=EdgeWeighted(Brest,Saintb,20)
    edge8=EdgeWeighted(Quimper,Vannes,20)
    edge3=EdgeWeighted(Vannes,Rennes,50)
    edge4=EdgeWeighted(Saintb,Rennes,50)
    edge5=EdgeWeighted(Rennes,Nantes,70)
    edge6=EdgeWeighted(Vannes,Nantes,70)
    edge7=EdgeWeighted(Nantes,Rennes,70)

    session.add_all([Brest,Quimper,Saintb,Vannes,Rennes,Nantes])
    session.commit()

## look at the relational database :
##{logname@hostname}sqlite3 graph.db
##sqlite> .headers on
##sqlite> .mode column
##sqlite> .width 10
##sqlite> .tables
##
##select * from edges;
##edge_id   above_id  below_id  
##--------  --------  --------
##1         1         2         
##sqlite> select * from nodes;
##node_id   name      
##-------   -------
##1         Brest     
##2         Quimper   
##sqlite> 
##
