# coding: utf-8

from random import randint, choice, sample
from Configuration import *
from PoliticalOrientation import Orientation
import Deffuant
# If you need to work on multiple graphs, use
# from Graphs_multiple import Graphs
from Graph import Graph

print("\n\t-".join(["Showing plots.", "N=number of nodes", "R=number of runs",
          "T=threshold", "C=convergence parameter", "D=density",
          "ASP=average shortest path length", "E=Edges"]))

graphs = []
statistics = []
for i in range(0, ISLANDS):
  inhabitantsAmount = randint(AGENTS_AMOUNT_MIN, AGENTS_AMOUNT_MAX)
  graphs.append(Graph(inhabitantsAmount))

  [graphName, inhabitantsAmount, density, asp, edgesAmount] = graphs[i].getInformation()
  print("%s (N=%i, R=%i, C=%.1f, D=%.2f, ASP=%.2f, E=%i):" % (graphName, inhabitantsAmount,
                        RUNS, CONVERGENCE_PARAMETER, density, asp, edgesAmount))

for i in range(RUNS):
  graphs = sample(graphs, len(graphs))
  for graphObject in graphs:
    graph = graphObject.graph
    statistic = graphObject.statistic

    statistic.addDominantColours(graph)
    if (i % EXCHANGE_STEPS) != 0:
      Deffuant.apply(graph)
    else:
      """Create the average agent of each graph and send them to
      each other graph to talk to all its nodes."""
      averageAgent = graphObject.createAverageAgent()
      graphsPermutation = sample(graphs, len(graphs))
      for otherGraphObject in graphsPermutation:
        if otherGraphObject is not graphObject:
          otherGraph = otherGraphObject.graph
          Deffuant.applyToAll(otherGraph, averageAgent)

# add final configuration and plot it:
for graphObject in graphs:
  statistic = graphObject.statistic
  statistic.addDominantColours(graph)
  statistic.plot()
