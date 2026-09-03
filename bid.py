class Bid:
    def __init__(self, candidate, bid_amount, player):
        self.candidate = candidate
        self.bid_amount = bid_amount
        self.player = player

    def __repr__(self):
        return f"Bid(candidate={self.candidate}, bid_amount={self.bid_amount})"