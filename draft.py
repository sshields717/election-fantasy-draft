# system that list candidates and their starting prices, 
# and allows all players to bid. turn based bidding, everyone must pass before the candidate is awarded. 
# Must give all players at least 1 chance to bid. If all pass, candidate is not rostered. After any player makes a bid, all players must pass. 
# If another bid is made, restart the loop until all the rest have passed.
# The order of candidates is the most expensive starting price to the least expensive starting price.
# The order of players is randomized each round.
import random
from bid import Bid

class Draft:
    def __init__(self, league):
        self.league = league
        self.current_candidate = None
        self.current_bid = None
        self.bidding_order = []
        self.passed_players = set()
        self.priced_out_players = set()  # Track players who have been priced out of bidding

    # a minimuim bid is the current bid + 1, or the starting price if there is no current bid. 
    def minimum_bid(self):
        return (self.current_bid.bid_amount + 1) if self.current_bid else self.current_candidate.starting_price
        
    def start_draft(self):
        # import candidates from the league
        candidates = self.league.candidates

        # Sort candidates by starting price (most expensive to least expensive)
        sorted_candidates = sorted(candidates, key=lambda c: c.starting_price, reverse=True)

        for candidate in sorted_candidates:
            self.current_candidate = candidate
            self.current_bid = None
            self.bidding_order = list(self.league.players)
            random.shuffle(self.bidding_order)  # Shuffle the bidding order
            self.passed_players.clear()
            self.priced_out_players.clear()  # Reset players priced out for this candidate

            print(f"Starting bidding for {candidate.name} (Starting Price: {candidate.starting_price})")

            # Continue bidding until all players have passed or are priced out, or until a bid is made and all others have passed
            while len(self.passed_players | self.priced_out_players) < (len(self.bidding_order) - 1 if self.current_bid else len(self.bidding_order)):
                for player in self.bidding_order:
                    # If a player has already passed or is priced out, skip their turn
                    if player in self.passed_players:
                        continue
                    if player in self.priced_out_players:
                        continue
                    if player == self.current_bid.player if self.current_bid else None:
                        continue

                    # if the player has less than the minumim budget of the current candidate, they are priced out
                    if player.budget_remaining() < self.minimum_bid():
                        print(f"{player.name} is priced out for {self.current_candidate.name}.")
                        self.priced_out_players.add(player)
                        continue

                    bid_amount = self.get_player_bid(player)
                    
                    if bid_amount is None:
                        print(f"{player.name} has passed.")
                        self.passed_players.add(player)
                    # if a player enters a bid that is lower than the current bid, it should not be accepted, and the player should be prompted to bid again or pass.
                    elif bid_amount >= self.minimum_bid():
                        self.current_bid = Bid(candidate, bid_amount, player)
                        print(f"{player.name} bids ${bid_amount} for {candidate.name}.")
                        # Reset passed players since a new bid was made
                        self.passed_players.clear()
                    else:
                        print(f"{player.name}'s bid of ${bid_amount} is too low. Must be higher than current bid.")

            if self.current_bid:
                winning_player = self.current_bid.player
                winning_player.roster.append(self.current_bid)
                print(f"{winning_player.name} wins {candidate.name} for ${self.current_bid.bid_amount}.")
            else:
                print(f"No bids for {candidate.name}. Candidate not rostered.")


    def get_player_bid(self, player):
        # Eventually we want to bake in logic for when there are all human players, which is the intent for the application. 
        # The AI bidding logic is just a placeholder for now.

        if player.name == "Human":
            while True:
                try:
                    bid_input = input(f"{player.name}, enter your bid for {self.current_candidate.name} (or 'pass' to pass): ")
                    if bid_input.lower() == 'pass':
                        return None
                    bid_amount = int(bid_input)
                    if bid_amount <= 0:
                        print("Bid must be a positive integer.")
                        continue
                    if bid_amount >= player.budget_remaining():
                        print(f"Bid exceeds your remaining budget of ${player.budget_remaining()}.")
                        continue
                    return bid_amount
                except ValueError:
                    print("Invalid input. Please enter a valid integer or 'pass'.")
        else:
            # AI bidding logic: Randomly decide to bid or pass
            if player.budget_remaining() < self.minimum_bid():
                print(f"{player.name} cannot bid due to insufficient budget.")
                self.priced_out_players.add(player)
                return None
 
            if random.choice([True, False]):
                bid_amount = random.randint(self.minimum_bid(), player.budget_remaining())
                return bid_amount
            else:
                return None

    def display_rosters(self):
        print("\nFinal Rosters:")
        for player in self.league.players:
            print(f"{player.name}'s Roster:")
            for bid in player.roster:
                print(f"  - {bid.candidate.name} at ${bid.bid_amount}")
            print(f"Remaining Budget: ${player.budget_remaining()}\n")
