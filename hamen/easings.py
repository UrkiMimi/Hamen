# hamen easings class
import math as Math

class Easings:
    """A collection of interpolation functions for baking animations
    """

    def easeLinear(x, y, time):
        return ((1 - time) * x) + (y * time)

    #easeOutSine(x, y, time)