# coding: utf-8

from Configuration import THRESHOLD, CONVERGENCE_PARAMETER, AGENTS_AMOUNT
from PoliticalOrientation import Orientation

def apply(graph):
  # TODO a heuristic would be nice to not draw the same pairs over and over again
  from random import randint

  applied = False
  while(not applied):
    n1_id = randint(0, AGENTS_AMOUNT-1)
    a1 = graph.node[n1_id]["Agent"]
    neighbours = graph.neighbors(n1_id)
    n2_rand = randint(0, len(neighbours)-1)
    try:
      n2_id = neighbours[n2_rand]
      a2 = graph.node[n2_id]["Agent"]

      if areInterestsSimilar(a1, a2):
        adjustInterests(graph, n1_id, n2_id)
        applied = True
    except IndexError:
      pass # do we ever end up here?

def areInterestsSimilar(a1, a2):
  """Takes each interest value and subtracts value_j from value_i.
  This is taken as an absolute value and summed up as a difference
  measure which will be averaged and tested against the threshold.
  Both a1 and a2 are Agents."""
  difference = 0
  for name, member in Orientation.__members__.items():
    difference += abs(a1.orientation[name] - a2.orientation[name])
  return (difference / len(Orientation) < THRESHOLD)

def adjustInterests(graph, n1_id, n2_id):
  """ Receives the graphs and the identifiers of the two agents.
  Applies the Deffuant step on both. n1OrientationP is the
  probability associated with the orientation of agent 1."""
  # TODO can we also directly work on the agents and rely on the graph being updated by reference?
  a1 = graph.node[n1_id]["Agent"]
  a2 = graph.node[n2_id]["Agent"]
  for name, member in Orientation.__members__.items():
    n1OrientationP = a1.orientation[name]
    n2OrientationP = a2.orientation[name]

    a1.orientation[name] = n1OrientationP + CONVERGENCE_PARAMETER * (n2OrientationP - n1OrientationP)
    a2.orientation[name] = n2OrientationP + CONVERGENCE_PARAMETER * (n1OrientationP - n2OrientationP)

  graph.node[n1_id]["Agent"] = a1
  graph.node[n2_id]["Agent"] = a2
