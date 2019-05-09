from enums import TransparencyLevel
from models import NecklaceStone


class JewelerManager:
    def __init__(self, stone_list=[]):
        self.stone_list = stone_list

    def __del__(self):
        print("Execute Manager")

    def add_stone(self, new_stone=NecklaceStone):
        self.stone_list.append(new_stone)

    def sort_stones_by_price(self, reverse=True):
        return sorted(self.stone_list, key=lambda stone: stone.carats,
                      reverse=reverse)

    def sort_stones_by_weight(self, reverse=False):
        return sorted(self.stone_list, key=lambda stone: stone.carats,
                      reverse=reverse)

    def find_stones_by_transparency(self, to_level=repr(TransparencyLevel),
                                    from_level=repr(TransparencyLevel)):
        return list(filter(lambda stone:
                           from_level <= repr(stone.transparency) <= to_level,
                           self.stone_list))

