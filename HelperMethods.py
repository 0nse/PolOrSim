# coding: utf-8

def addColoursForAllGraphs(graphs, globalOrientationCounts, globalStatistic):
  """Add colours of all graphs to their respecitve
  Statistics object and modify the global statistics."""
  for graphObject in graphs:
    statistic = graphObject.statistic
    orientationCounts = statistic.calculateAndAddDominantColours(graphObject.graph)
    for name in orientationCounts:
      globalOrientationCounts[name] += orientationCounts[name]
  globalStatistic.addDominantColours(globalOrientationCounts, len(graphs))

def createEmptyOrientationDictionary():
  """Return a dictionary with all keys set from
  Orientation but all values set to 0."""
  from PoliticalOrientation import Orientation

  orientation = {}
  for name, member in Orientation.__members__.items():
    orientation[name] = 0
  return orientation

