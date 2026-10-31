# hamen easings class
import math as Math

class Easings:
    """A collection of interpolation functions for baking animations
    """

    def easeLinear(x, y, time):
        return ((1 - time) * x) + (y * time)

    # Ease out
    def easeOutBounce(x):
        n1 = 7.5625
        d1 = 2.75

        if (x < 1 / d1):
            return n1 * x * x
        elif (x < 2 / d1):
            return (n1 * (x - 1.5 / d1) * x + 0.75)
        elif (x < 2.5 / d1):
            return (n1 * (x - 2.25 / d1) * x + 0.9375)
        else:
            return (n1 * (x - 2.625 / d1) * x + 0.984375)

    # Ease in
    def easeInSine(x):
        return (1 - Math.cos((x * Math.pi) / 2))
    def easeInCubic(x):
        return (x * x * x)
    def easeInQuint(x):
        return (x * x * x * x * x)
    def easeInCirc(x):
        return (1 - Math.sqrt(1 - Math.pow(x, 2)))
    def easeInElastic(x):
        c4 = (2 * Math.pi) / 3
        return 0 if x == 0 else 1 if x == 1 else (-1(Math.pow(2, 10 * x - 10) * Math.sin((x * 10 - 10.75) * c4)))
    def easeInQuad(x):
        return (x * x)
    def easeInQuart(x):
        return (x * x * x * x)
    def easeInExpo(x):
        return (0 if x == 0 else Math.pow(2, 10 * x - 10))
    def easeInBack(x):
        c1 = 1.70158
        c3 = c1 + 1
        return (c3 * x * x * x - c1 * x * x)
    
    def easeInBounce(x):
        return (1 - Easings.easeOutBounce(1 - x))

    # Ease in/out
    def easeInOutSine(x):
        return -1(Math.cos(Math.pi * x) - 1) / 2
    def easeInOutCubic(x):
        return (4 * x * x * x) if x < 0.5 else (1 - Math.pow(-2 * x + 2, 3) / 2)
    def easeInOutQuint(x):
        return (16 * x * x * x * x * x) if x < 0.5 else (1 - Math.pow(-2 * x + 2, 5) / 2)
    def easeInOutCirc(x):
        return ((1 - Math.sqrt(1 - Math.pow(2 * x, 2))) / 2) if x < 0.5 else ((Math.sqrt(1 - Math.pow(-2 * x + 2, 2)) + 1) / 2)
    def easeInOutElastic(x):
        c5 = ((2 * Math.pi) / 4.5)
        return 0 if x == 0 else 1 if x == 1 else (-1(Math.pow(2, 20 * x - 10) * Math.sin((20 * x - 11.125) * c5)) / 2) if x < 0.5 else ((Math.pow(2, 20 * x - 10) * Math.sin((20 * x - 11.125) * c5)) / 2 + 1)