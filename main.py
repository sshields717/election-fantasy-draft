# Initiating this will initiate the draft process for the league. 
# First, the admin will add players to the league. Then, the draft will be initiated.
# It will go through each candidate and allow players to bid on them in a randomized order. 
# The bidding will continue until all players have passed on a candidate, at which point the candidate will be assigned to the highest bidder. 
# The process will repeat for all candidates in the league.
# Initiating the draft should give the user the option to add up to 5 players to the league. The user will be able to input the names of the players, and the draft will be initiated with those players.
 

def main():
    from league import League
    from draft import Draft
    from player import Player

    # Create a league with a name, empty players list, and candidates list
    league_name = input("Enter the name of your league: ")
    league_budget = int(input("Enter the budget for each player (hit enter for default of 100): ") or "100")
    league = League(league_name, [], league_budget, [])
    league.add_candidates()

    # Add players to the league
    num_players = int(input("Enter the number of players in the league (up to 5): "))
    for i in range(num_players):
        player_name = input(f"Enter the name of player (type Human for human player) {i + 1}: ")
        player = Player(player_name, league.budget_per_player)
        league.add_player(player)

    # Start the draft
    draft = Draft(league)
    draft.start_draft()
    
    # Display final rosters after the draft is complete
    draft.display_rosters()

if __name__ == "__main__":
    main() 
    


