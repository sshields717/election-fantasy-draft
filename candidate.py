class Candidate:
    def __init__(self, name, party, starting_price):
        self.name = name
        self.party = party
        self.starting_price = starting_price

    def __repr__(self):
        return f"Candidate(name={self.name}, party={self.party}, starting_price={self.starting_price})"

