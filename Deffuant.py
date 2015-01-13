# coding: utf-8

from Configuration import CONVERGENCE_PARAMETER
from PoliticalOrientation import Orientation

def apply(graph):
  """Choose an agent and one of his neighbours randomly. Then,
  check their difference in orientations. If the difference is
  low enough to be accepted by one (or both) agents, the
  affected agents' orientations are modified. Returns True if
  at least one of two agents must have accepted the opinion of
  the other agent."""
  from random import randint

  n1_id = randint(0, len(graph) - 1)
  a1 = graph.node[n1_id]["Agent"]
  neighbours = graph.neighbors(n1_id)
  n2_rand = randint(0, len(neighbours)-1)
  try:
    n2_id = neighbours[n2_rand]
    a2 = graph.node[n2_id]["Agent"]

    difference = calculateOrientationDifference(a1, a2)
    applied = adjustInterestsIfTolerantEnough(a1, a2, difference)
    return adjustInterestsIfTolerantEnough(a2, a1, difference) or applied
  except IndexError:
    return False

def applyToAll(graph, averageAgent):
  """Simulate the averageAgent meeting all agents of the graph
  and apply the deffuant step where possible."""
  for nodeId in graph.nodes_iter():
    currentAgent = graph.node[nodeId]["Agent"]
    difference = calculateOrientationDifference(currentAgent, averageAgent)
    adjustInterestsIfTolerantEnough(currentAgent, averageAgent, difference)


def calculateOrientationDifference(a1, a2):
  """Takes each interest value and subtracts value_j from value_i.
  This is taken as an absolute value and summed up as a difference
  measure which will be averaged."""
  difference = 0
  for name, member in Orientation.__members__.items():
    difference += abs(a1.orientation[name] - a2.orientation[name])
  return (difference / len(Orientation))

def adjustInterestsIfTolerantEnough(a1, a2, difference):
  """ Applies the Deffuant step on agent a1 if the difference
  in orientations lower than its tolerance. Returns True on
  application and false else."""
  if difference < a1.tolerance:
    for name, member in Orientation.__members__.items():
      a1.orientation[name] = a1.orientation[name] + CONVERGENCE_PARAMETER * (a2.orientation[name]- a1.orientation[name])
    return True
  else:
    return False
