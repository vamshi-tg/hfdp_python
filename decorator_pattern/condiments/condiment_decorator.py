from ..beverages.beverage import Beverage
from abc import ABCMeta, abstractmethod


class CondimentDecorator(Beverage):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_description(self):
        pass