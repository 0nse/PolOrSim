# coding: utf-8

import networkx as nx

class Graph:
  def __init__(self, nodesAmount):
    """Create a Barabási-Albert graph."""
    from Configuration import LINK_CREATION_PROBABILITY, INITIAL_CONNECTIONS

    self.graph = nx.barabasi_albert_graph(nodesAmount, INITIAL_CONNECTIONS)
    self.initialiseAgentNetwork()

  def getInformation(self):
    """Returns a list of (statistical) information about the graph."""
    return ["Barabási-Albert", len(self.graph), nx.density(self.graph), nx.average_shortest_path_length(self.graph), len(nx.edges(self.graph))]

  def initialiseAgentNetwork(self):
    """Initialises agents on the graph nodes. It would be possible
    to associate the values directly with the nodes instead of
    using an object."""
    from Agent import Agent

    for nodeId in self.graph.nodes_iter():
      self.graph.node[nodeId]["Agent"] = Agent()
