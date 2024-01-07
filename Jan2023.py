class Wallet:
    def __init__(self, money: int, card: int):
        self.money = money

    def receive_morning_money(self):
        self.money += 10000

    def grandma_top_up(self):
        self.card = 5


class Pocket:
    def __init__(self, wallet: int):
        self.wallet = wallet





