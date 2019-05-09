from models.NecklaceStone import NecklaceStone
from enums.CleavageLevel import CleavageLevel
from enums.TransparencyLevel import TransparencyLevel


class Gem(NecklaceStone):
    def __init__(self, name="No name", transparency_level=TransparencyLevel,
                 mine_place="No name", price=0.0, carats=0.0,
                 cleavage_level=CleavageLevel):
        super().__init__(name, transparency_level, mine_place, price, carats)
        self.cleavage_level = cleavage_level

    def __str__(self):
        return str(super().__str__()) + "\n Level of cleavage: " + str(
            self.cleavage_level)
