# coding: utf-8

from Configuration import CONVERGENCE_PARAMETER, AGENTS_AMOUNT
from PoliticalOrientation import Orientation

def apply(graph):
  """Choose an agent and one of his neighbours randomly. Then,
  check their difference in orientations. If the difference is
  low enough to be accepted by one (or both) agents, the
  affected agents' orientations are modified. For this Deffuant
  step to finish, at least one of two agents must have accepted
  the opinion of the other agent."""
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

      difference = calculateOrientationDifference(a1, a2)
      applied = adjustInterestsIfTolerantEnough(a1, a2, difference)
      applied = adjustInterestsIfTolerantEnough(a2, a1, difference) or applied
    except IndexError:
      pass # do we ever end up here?

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
