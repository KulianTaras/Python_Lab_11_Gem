from enums import TransparencyLevel, Origin
from models.NecklaceStone import NecklaceStone


class SemiPreciousStone(NecklaceStone):
    def __init__(self, name="No name", transparency_level=TransparencyLevel,
                 mine_place="No name", price=0.0, carats=0.0,
                 origin=Origin):
        super().__init__(name, transparency_level, mine_place, price, carats)
        self.origin = origin

    def __str__(self):
        return str(super().__str__()) + "\n Origin: " + str(self.origin)
