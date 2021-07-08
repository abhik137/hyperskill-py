class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        total_cents = (self.dollars + deposit_dollars) * 100 + self.cents + deposit_cents
        self.dollars = total_cents // 100
        self.cents = total_cents % 100
