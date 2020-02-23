from .beverage import Beverage


class DarkRoast(Beverage):

    def __init__(self):
        self._description = "Dark Roast"

    def cost(self):
        return 0.99