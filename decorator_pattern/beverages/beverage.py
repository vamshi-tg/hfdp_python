from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):

    def __init__(self):
        self._description = "Unknown Description"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass