class Character:
    def __init__(self, name:str, level:int=10):
        self.name = name
        self.level = level
        self.exp = 0
        self.required_exp = 200

    def level_up(self):

        self.exp = 0
        self.required_exp += 100
        self.level += 1


class Lala(Character):
    def __init__(self, name: str, luk: int = 10, level: int = 10):
        super().__init__(name, level)
        self.luk = 10

    def spirit(self):
        print(f"{self.name}use spirit! luk_ :{self.luk}")






