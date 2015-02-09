# coding: utf-8

from random import randint, choice, sample
from Configuration import *
import Deffuant
from Graph import Graph
from Statistic import Statistic
from HelperMethods import *

print("\n\t-".join(["Plots will be saved to disk.", "N=number of nodes", "R=number of runs",
          "T=threshold", "C=convergence parameter", "D=density",
          "ASP=average shortest path length", "E=Edges"]))

graphs = []
statistics = []
for i in range(0, VILLAGES):
  inhabitantsAmount = randint(AGENTS_AMOUNT_MIN, AGENTS_AMOUNT_MAX)
  graphs.append(Graph(inhabitantsAmount))

globalStatistic = Statistic()
globalOrientationCounts = createEmptyOrientationDictionary()
addColoursForAllGraphs(graphs, globalOrientationCounts, globalStatistic)

for i in range(RUNS):
  globalOrientationCounts = createEmptyOrientationDictionary()
  graphs = sample(graphs, len(graphs))

  for graphObject in graphs:
    graph = graphObject.graph
    if (i % EXCHANGE_STEPS) != 0:
      Deffuant.apply(graph)
    else:
      """Create the average agent of each graph and send them to
      every other graph to talk to all its nodes."""
      averageAgent = graphObject.createAverageAgent()
      graphsPermutation = sample(graphs, len(graphs))
      for otherGraphObject in graphsPermutation:
        if otherGraphObject is not graphObject:
          otherGraph = otherGraphObject.graph
          Deffuant.applyToAll(otherGraph, averageAgent)
  addColoursForAllGraphs(graphs, globalOrientationCounts, globalStatistic)

# add final configuration and plot it:
globalStatistic.plot("Average orientation of all islands.")

for graphObject in graphs:
  statistic = graphObject.statistic
  [graphName, inhabitantsAmount, density, asp, edgesAmount] = graphObject.getInformation()
  title = ("%s (N=%i, R=%i, C=%.1f, D=%.2f, ASP=%.2f, E=%i):" % (graphName, inhabitantsAmount,
                        RUNS, CONVERGENCE_PARAMETER, density, asp, edgesAmount))
  statistic.plot(title)
