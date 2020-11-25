# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Node(Base) :
    __tablename__ ='nodes'
    node_id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name="n"):
        self.name = name
    def __repr__(self):
        return "<Node(%s)>" % (self.name)
    def __repr__(self):
        return "<" + self.__class__.__name__ + "({})>".format(self.name)


    def get_name(self):
        return self.name
    def set_name(self,name):
             self.name = name
    def above_neighbors(self):
        return [x.node_above for x in self.previous_edgesweighted]

    def below_neighbors(self):
        return [x.node_below for x in self.following_edgesweighted]

class Edge(Base) :
    __tablename__ ='edges'

    edge_id = Column(Integer, primary_key=True)

    above_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_above = relationship(Node,
                              primaryjoin=above_id == Node.node_id,
                              backref='following_edges')
    below_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_below = relationship(Node,
                              primaryjoin=below_id == Node.node_id,
                              backref='previous_edges')


                               

    def __init__(self,n1,n2):
        self.node_above=n1
        self.node_below=n2

    def __repr__(self):
        return "<" + self.__class__.__name__ + "({},{})>".format(self.node_above,self.node_below)

    def get_node_above(self):
        return self.node_above
    def set_node_above(self,node):
        self.node_above=node
    def get_node_below(self):
        return self.node_below
    def set_node_below(self,node):
        self.node_below=node


class EdgeWeighted(Edge) :
    __tablename__ = "edges_weighted"
    __mapper_args__ = {
       'polymorphic_identity': 'weighted',
        "concrete" : True
    }
    edge_weighted_id = Column(Integer, primary_key=True)
    weight = Column(Integer)

    above_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_above = relationship(Node,
                              primaryjoin=above_id == Node.node_id,
                              backref='following_edgesweighted')
    below_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_below = relationship(Node,
                              primaryjoin=below_id == Node.node_id,
                              backref='previous_edgesweighted')

    def __init__(self,n1,n2,w):
        self.node_above=n1
        self.node_below=n2 
        self.weight=w                         

    def get_weight(self): 
        return self.weight         


class EdgeColored(Edge) :
    __tablename__ = "edges_Colored"
    __mapper_args__ = {
       'polymorphic_identity': 'colored',
        "concrete" : True
    }
    edge_colored_id = Column(Integer, primary_key=True)
    color = Column(String(50))

    above_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_above = relationship(Node,
                              primaryjoin=above_id == Node.node_id,
                              backref='following_edgescolored')
    below_id = Column(Integer,ForeignKey('nodes.node_id'))
    node_below = relationship(Node,
                              primaryjoin=below_id == Node.node_id,
                              backref='previous_edgescolored')

    def __init__(self,n1,n2,c):
        self.node_above=n1
        self.node_below=n2 
        self.color=c                     

    def get_color(self): 
        return self.color                