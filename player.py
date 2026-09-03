
class Player:
    def __init__(self, name, budget_total):
        self.name = name
        self.budget_total = budget_total
        self.roster = []

    def budget_remaining(self):
        spent = sum(bid.bid_amount for bid in self.roster)
        return self.budget_total - spent

    