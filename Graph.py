# coding: utf-8

import networkx as nx

class Graph:
  def __init__(self):
    """Create a Barabási-Albert graph."""
    from Configuration import LINK_CREATION_PROBABILITY, INITIAL_CONNECTIONS
    from Configuration import AGENTS_AMOUNT as NODES_AMOUNT

    self.graph = nx.barabasi_albert_graph(NODES_AMOUNT, INITIAL_CONNECTIONS)
    self.initialiseAgentNetwork()

  def buildDict(self):
    """Returns a dict with the name as key and the graphs as
    value together with some statistical information."""
    return {"Barabási-Albert" : [self.graph, nx.density(self.graph), nx.average_shortest_path_length(self.graph), len(nx.edges(self.graph))]}

  def initialiseAgentNetwork(self):
    """Initialises agents on the graph nodes. It would be possible
    to associate the values directly with the nodes instead of
    using an object."""
    from Agent import Agent

    for nodeId in self.graph.nodes_iter():
      self.graph.node[nodeId]["Agent"] = Agent()
