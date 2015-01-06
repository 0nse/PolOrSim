# coding: utf-8

import networkx as nx

class Graphs:
  """This class can be used to generate graphs. It allows
  the generation of multiple or just one graph with values
  defined inside the Configuration file.
  The default is to only create a Barabási-Albert graph. If
  that is all you need, you can shrink this class to approx.
  15 lines."""

  def __init__(self, types=["ba"]):
    """Create one or multiple graphs. Possible parameters are:
    "ba" : Barabási-Albert (default)
    "er" : Erdős-Renyi
    "ws" : Watts-Strogatz
    or a combination of those."""
    from Configuration import LINK_CREATION_PROBABILITY, INITIAL_CONNECTIONS
    from Configuration import AGENTS_AMOUNT as NODES_AMOUNT

    if len(types) == 1 and types[0] not in ["ba", "er", "ws"]:
        types = ["ba"]

    self.graphs = {}

    for graphType in types:
      if graphType == "ba":
        # preferential attachment graph (follows a power law), where 20 edges from existing
        # nodes will be attached to a new one:
        self.graphs[graphType] = nx.barabasi_albert_graph(NODES_AMOUNT, INITIAL_CONNECTIONS)
      elif graphType == "er":
        self.graphs[graphType] = nx.erdos_renyi_graph(NODES_AMOUNT, LINK_CREATION_PROBABILITY)
      elif graphType == "ws":
        # small world random graph with every node connected to 20 of the nearest neighbours:
        self.graphs[graphType] = nx.newman_watts_strogatz_graph(NODES_AMOUNT, INITIAL_CONNECTIONS + 8, LINK_CREATION_PROBABILITY + 0.2)

    self.types = types
    self.initialiseAgentNetwork()

  def buildDict(self):
    """Returns a dict with the name as key and the graphs as
    value together with some statistical information."""
    result = {}
    for graphType in self.types:
      if graphType == "ba":
        graphName = "Barabási-Albert"
      elif graphType == "er":
        graphName = "Erdős–Rényi"
      elif graphType == "ws":
        graphName = "Watts–Strogatz"

      graph = self.graphs[graphType]
      d = {graphName : [graph, nx.density(graph), nx.average_shortest_path_length(graph), len(nx.edges(graph))]}
      result.update(d)
    return result

  def initialiseAgentNetwork(self):
    """Initialises agents on the graph nodes. It would be possible
    to associate the values directly with the nodes instead of
    using an object."""
    from Agent import Agent

    for graphType in self.graphs:
      graph = self.graphs[graphType]
      for nodeId in graph.nodes_iter():
        graph.node[nodeId]["Agent"] = Agent()

  def __len__(self):
      """The lengths is defined as the number of created graphs"""
      return len(self.types)
