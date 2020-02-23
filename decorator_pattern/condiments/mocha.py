from .condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return f"{self.beverage.get_description()} Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20