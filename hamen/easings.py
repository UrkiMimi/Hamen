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
    def easeOutExpo(x):
        return 1 if x == 1 else 1 - Math.pow(2, -10 * x)
    def easeOutElastic(x):
        c4 = (2 * Math.PI) / 3
        return 0 if x == 0 else 1 if x == 1 else Math.pow(2, -10 * x) * Math.sin((x * 10 - 0.75) * c4) + 1
    def easeOutQuart(x):
        return 1 - Math.pow(1 - x, 4)
    def easeOutQuad(x):
        return 1 - (1 - x) * (1 - x)
    def easeOutCirc(x):
        return Math.sqrt(1 - Math.pow(x - 1, 2))
    def easeOutQuint(x):
        return 1 - Math.pow(1 - x, 5)
    def easeOutCubic(x):
        return 1 - Math.pow(1 - x, 3)
    def easeOutSine(x):
        return Math.sin((x * Math.PI) / 2)
    def easeOutBack(x):
        c1 = 1.70158
        c3 = c1 + 1

        return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2)


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
    def easeInOutQuad(x):
        return 1 - 2 * x * x if x < 0.5 else 1 - Math.pow(-2 * x + 2, 2) / 2
    def easeInOutQuart(x):
        return 8 * x * x * x * x if x < 0.5 else 1 - Math.pow(-2 * x + 2, 4) / 2
    def easeInOutExpo(x):
        return Easings.easeOutExpo(x) if x < 0.5 else Easings.easeInExpo(x)
    def easeInOutBack(x):
        return Easings.easeOutBack(x) if x < 0.5 else Easings.easeInBack(x)
    def easeInOutBounce(x):
        return Easings.easeOutBounce(x) if x < 0.5 else Easings.easeInBounce(x)
    def easeInOutCirc(x):
        return ((1 - Math.sqrt(1 - Math.pow(2 * x, 2))) / 2) if x < 0.5 else ((Math.sqrt(1 - Math.pow(-2 * x + 2, 2)) + 1) / 2)
    def easeInOutElastic(x):
        c5 = ((2 * Math.pi) / 4.5)
        return 0 if x == 0 else 1 if x == 1 else (-1(Math.pow(2, 20 * x - 10) * Math.sin((20 * x - 11.125) * c5)) / 2) if x < 0.5 else ((Math.pow(2, 20 * x - 10) * Math.sin((20 * x - 11.125) * c5)) / 2 + 1)