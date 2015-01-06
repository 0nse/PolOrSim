# coding: utf-8

class Agent:
  def __init__(self):
    """On class creation, randomly generate attributes."""
    from random import uniform
    from Configuration import MAX_STUBBORNNESS

    self.orientation = {}

    self.stubbornness_percent = uniform(0, MAX_STUBBORNNESS)
    self.initialiseOrientation()

  def initialiseOrientation(self):
    """Set orientations randomly as probabilities.
    max(sum(orientation(node))) = 1
    min(sum(orientation(node))) = 0"""
    from PoliticalOrientation import Orientation
    from random import choice, randint

    orientationsLeft = [name for name, member in Orientation.__members__.items()]
    percentageLeft = 100
    for i in range(0, len(Orientation)):
      percentage = randint(0, percentageLeft)
      percentageLeft -= percentage

      # randomly pick an orientation to prevent favouring one:
      name = choice(orientationsLeft)
      orientationsLeft.remove(name)
      self.orientation[name] = percentage / 100 # make it a probability
