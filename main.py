from managers.jeweler_manager import JewelerManager
from models.gem import Gem
from models.semi_precious_stone import SemiPreciousStone
from models.necklace_stone import NecklaceStone
from enums.transparency_level import TransparencyLevel
from enums.cleavage_level import CleavageLevel
from enums.origin import Origin


def main():
    object_1 = Gem("Gem", TransparencyLevel.ZERO, "Ukraine", 22.0, 1.2,
                   CleavageLevel.MIDDLE)
    manager = JewelerManager()

    diamond = Gem("Diamond", TransparencyLevel.HIGH, "Israel", 5200, 1.2,
                  CleavageLevel.PERFECT)
    amethyst = SemiPreciousStone("Amethyst", TransparencyLevel.MIDDLE,
                                 "Russian", 1200, 0.9, Origin.NATURAL)
    hangam = NecklaceStone("Hangam", TransparencyLevel.LOW, "Ukraine", 200, 0.7)

    manager.add_stone(object_1)
    manager.add_stone(diamond)
    manager.add_stone(amethyst)
    manager.add_stone(hangam)

    print(*manager.sort_stones_by_price(True), sep='\n')
    print("---------------------------------------------------")
    print(*manager.sort_stones_by_weight(False), sep='\n')
    print("---------------------------------------------------")
    print(*manager.find_stones_by_transparency(
        repr(TransparencyLevel.ZERO),repr(TransparencyLevel.LOW)), sep='\n')


if __name__ == "__main__":
    main()
