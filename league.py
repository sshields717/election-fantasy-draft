# the container for a set of players and avialable candidates.
import json
from candidate import Candidate

class League:
    def __init__(self, league_name, players, budget_per_player, candidates):
        self.league_name = league_name
        self.players = players
        self.budget_per_player = budget_per_player
        self.candidates = candidates

    def __repr__(self):
        return f"League(players={self.players}, candidates={self.candidates})"

    # add a player to the league's players list
    def add_player(self, player):
        self.players.append(player)

    # import candidates list from JSON file to the league's candidates list
    def add_candidates(self):
        with open('candidates.json', 'r') as file:
            candidates_raw = json.load(file)

        # Make a bunch of Candidate objects from the JSON data and add them to the candidates list.
        for candidate_data in candidates_raw:
            candidate = Candidate(**candidate_data)
            self.candidates.append(candidate)



