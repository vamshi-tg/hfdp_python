from .beverages.dark_roast import DarkRoast
from .beverages.espresso import Espresso

from .condiments.mocha import Mocha
from .condiments.whip import Whip

if __name__ == "__main__":
    beverage = DarkRoast()
    print(f"{beverage.get_description()} - {beverage.cost()}")

    beverage_2 = Espresso()
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    print(f"{beverage_2.get_description()} - {beverage_2.cost()}")