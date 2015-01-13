# coding: utf-8

import networkx as nx
from Agent import Agent
from Statistic import Statistic

class Graph:
  def __init__(self, nodesAmount):
    """Create a pre-populated Barabási-Albert graph."""
    from Configuration import LINK_CREATION_PROBABILITY, INITIAL_CONNECTIONS

    self.graph = nx.barabasi_albert_graph(nodesAmount, INITIAL_CONNECTIONS)
    self.statistic = Statistic()
    self.initialiseAgentNetwork()

  def getInformation(self):
    """Returns a list of (statistical) information about the graph."""
    return ["Barabási-Albert", len(self.graph), nx.density(self.graph), nx.average_shortest_path_length(self.graph), len(nx.edges(self.graph))]

  def initialiseAgentNetwork(self):
    """Initialises agents on the graph nodes. It would be possible
    to associate the values directly with the nodes instead of
    using an object."""
    for nodeId in self.graph.nodes_iter():
      self.graph.node[nodeId]["Agent"] = Agent(True)

  def createAverageAgent(self):
    """Calculate the average agent"""
    from PoliticalOrientation import Orientation

    averageAgent = Agent(False)

    for nodeId in self.graph.nodes_iter():
      currentAgent = self.graph.node[nodeId]["Agent"]

      for name, member in Orientation.__members__.items():
        averageAgent.orientation[name] += currentAgent.orientation[name]

    for key, value in averageAgent.orientation.items():
      averageAgent.orientation[key] /= len(self.graph)

    return averageAgent
