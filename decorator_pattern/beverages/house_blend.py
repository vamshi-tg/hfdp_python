from .beverage import Beverage


class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend"

    def cost(self):
        return 0.89