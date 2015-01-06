# coding: utf-8

import itertools
from random import randint, choice
# force float division in python2:
# from __future__ import division
from Configuration import *
from PoliticalOrientation import Orientation
import Deffuant
# If you want to generate graphs with models other than Barabási-Albert or want
# to run this simulation on multiple graphs at once,
# @see 2d254fc82d95c599dfb903b959064f4e1ebcc2ae
from Graph import Graph
from Statistics import Statistics

print("\n\t-".join(["Showing plots.", "N=number of nodes", "R=number of runs",
          "T=threshold", "C=convergence parameter", "D=density",
          "ASP=average shortest path length", "E=Edges"]))
# TODO: islands
# TODO: TVs (generalisation of Agents)
baGraph = Graph()
graph = baGraph.graph
[graphName, density, asp, edgesAmount] = baGraph.getInformation()
print("%s (N=%i, R=%i, C=%.1f, D=%.2f, ASP=%.2f, E=%i):" % (graphName,
                     AGENTS_AMOUNT, RUNS, CONVERGENCE_PARAMETER, density,
                     asp, edgesAmount))

orientationAtT = Statistics()

for j in range(RUNS):
  orientationAtT.addDominantColours(graph)
  Deffuant.apply(graph)

# add final configuration and plot it:
orientationAtT.addDominantColours(graph)
orientationAtT.plot()
