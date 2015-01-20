# coding: utf-8
from PoliticalOrientation import Orientation

def createEmptyOrientationDictionary():
  """Calculate the average agent"""
  orientation = {}
  for name, member in Orientation.__members__.items():
    orientation[name] = 0
  return orientation

class Agent:
  def __init__(self, generateInterests):
    """On class creation, randomly generate attributes if
    generateInterests is True. Else all attributes are 0."""
    from random import uniform
    from Configuration import MAX_TOLERANCE

    self.orientation = {}

    self.tolerance = uniform(0, MAX_TOLERANCE)
    if generateInterests:
      self.initialiseOrientation()
    else:
      self.orientation = createEmptyOrientationDictionary()


  def initialiseOrientation(self):
    """Set orientations randomly as probabilities.
    max(sum(orientation(node))) = 1
    min(sum(orientation(node))) = 0"""
    from random import randint, sample

    orientationNames = sample([name for name, member in Orientation.__members__.items()], len(Orientation))
    percentageLeft = 100
    for name in orientationNames:
      percentage = randint(0, percentageLeft)
      percentageLeft -= percentage
      self.orientation[name] = percentage / 100 # make it a probability
