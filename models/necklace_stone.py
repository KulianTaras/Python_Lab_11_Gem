from enums import transparency_level


class NecklaceStone:

    def __init__(self, name="No name", transparency_level=transparency_level,
                 mine_place="No name", price=0.0, carats=0.0):
        self.name = name
        self.transparency = transparency_level
        self.country = mine_place
        self.price = price
        self.carats = carats

    def __str__(self):
        return " Name: " + self.name + "\n Transparency: " +\
                str(self.transparency) + "\n Country = " + self.country +\
               "\n Price = " + str(self.price) + "\n Weight in carats = " +\
               str(self.carats)

    def __del__(self):
        print("Destroy", self.name)
