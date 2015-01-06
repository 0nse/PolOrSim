# coding: utf-8

from PoliticalOrientation import Orientation
from Configuration import AGENTS_AMOUNT, RUNS

class Statistics:
  def __init__(self):
    """Create a dictionary of orientations."""
    self.dominantColours = {}
    for orientation in Orientation:
      self.dominantColours[orientation.name] = []

  def addDominantColours(self, graph):
    """Iterates over the whole graph and sums up for how many nodes
    a certain colour was dominant. Results are stored in
    self.dominantColours as a percentage value."""
    orientationCounts = {orientation.name : 0 for orientation in Orientation}
    for nodeId in graph.nodes_iter():
      agent = graph.node[nodeId]["Agent"]
      highestValue = ("none", -1)

      for name, member in Orientation.__members__.items():
        value = agent.orientation[name]
        if value > highestValue[1]:
          highestValue = (name, value)
      orientationCounts[highestValue[0]] += 1 # reference or value? TODO

    # add all counts including the dominant colour:
    for name in orientationCounts:
      self.dominantColours[name].append(orientationCounts[name] / AGENTS_AMOUNT)

  def plot(self):
    from matplotlib import pyplot
    for (name, amounts) in self.dominantColours.items():
      colour = Orientation[name].value
      pyplot.plot(range(RUNS+1), amounts, color=colour, label=name)

    # Place a legend above this legend, expanding itself to
    # fully use the given bounding box:
    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
                  ncol=2, mode="expand", borderaxespad=0.)
    pyplot.show()
