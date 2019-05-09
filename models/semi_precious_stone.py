from enums import transparency_level, origin
from models.necklace_stone import NecklaceStone


class SemiPreciousStone(NecklaceStone):
    def __init__(self, name="No name", transparency_level=transparency_level,
                 mine_place="No name", price=0.0, carats=0.0,
                 origin=origin):
        super().__init__(name, transparency_level, mine_place, price, carats)
        self.origin = origin

    def __str__(self):
        return str(super().__str__()) + "\n Origin: " + str(self.origin)
