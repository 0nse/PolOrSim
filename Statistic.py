# coding: utf-8

from PoliticalOrientation import Orientation
from Configuration import RUNS

class Statistic:
  def __init__(self):
    """Create a dictionary of orientations."""
    self.dominantColours = {}
    for orientation in Orientation:
      self.dominantColours[orientation.name] = []

  def calculateAndAddDominantColours(self, graph):
    """Iterates over the whole graph and sums up for how many nodes
    a certain colour was dominant. Results are stored in
    self.dominantColours as a percentage value. Furthermore returns
    the counts for further processing."""
    orientationCounts = {orientation.name : 0 for orientation in Orientation}
    for nodeId in graph.nodes_iter():
      agent = graph.node[nodeId]["Agent"]
      highestValue = ("none", -1)

      for name, member in Orientation.__members__.items():
        value = agent.orientation[name]
        if value > highestValue[1]:
          highestValue = (name, value)
      orientationCounts[highestValue[0]] += 1

    # add all counts including the dominant colour:
    return self.addDominantColours(orientationCounts, len(graph))

  def addDominantColours(self, orientationCounts, amount):
    """Add alls colour counts and normalises them on the amount provided."""
    normalisedOrientation = {}
    for name in orientationCounts:
      value = orientationCounts[name] / amount
      self.dominantColours[name].append(value)
      normalisedOrientation[name] = value
    return normalisedOrientation

  def plot(self, title=None):
    from matplotlib import pyplot
    from datetime import datetime
    from pylab import savefig

    for (name, amounts) in self.dominantColours.items():
      colour = Orientation[name].value
      pyplot.plot(range(RUNS+1), amounts, color=colour, label=name)

    # Place a legend above this legend, expanding itself to
    # fully use the given bounding box:
    legend = pyplot.legend(bbox_to_anchor=(0.5, -0.1), loc=9,
                           ncol=2,
                  title=title)
    pyplot.xlabel('Runs')
    pyplot.ylabel('Normalised orientation')

    savefig('./plots/graph_%s.png' % datetime.now().isoformat(),
            dpi=300, bbox_inches="tight", additional_artists=[].append(legend))
    pyplot.close()
