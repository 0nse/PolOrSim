# coding: utf-8

import itertools
from random import randint, choice
from Configuration import *
from PoliticalOrientation import Orientation
import Deffuant
# If you need to work on multiple graphs, use
# from Graphs_multiple import Graphs
from Graph import Graph
from Statistics import Statistics

print("\n\t-".join(["Showing plots.", "N=number of nodes", "R=number of runs",
          "T=threshold", "C=convergence parameter", "D=density",
          "ASP=average shortest path length", "E=Edges"]))
# TODO: TVs (generalisation of Agents)
graphs = []
for i in range(0, ISLANDS):
  inhabitantsAmount = randint(AGENTS_AMOUNT_MIN, AGENTS_AMOUNT_MAX)
  graphs.append(Graph(inhabitantsAmount))

  [graphName, inhabitantsAmount, density, asp, edgesAmount] = graphs[i].getInformation()
  print("%s (N=%i, R=%i, C=%.1f, D=%.2f, ASP=%.2f, E=%i):" % (graphName, inhabitantsAmount,
                        RUNS, CONVERGENCE_PARAMETER, density, asp, edgesAmount))

orientationAtT = Statistics()
for i in range(RUNS):

  for graphObject in graphs:
    graph = graphObject.graph
    orientationAtT.addDominantColours(graph)
    if (i % EXCHANGE_STEPS) != 0:
      Deffuant.apply(graph)
    else:
      graphObject.createAverageAgent()
      # TODO: exchange agent orientations

# add final configuration and plot it:
orientationAtT.addDominantColours(graph)
orientationAtT.plot()
