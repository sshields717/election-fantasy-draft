# Fantasy Election Draft — Planning Steps 1–4

## Step 1: One-Sentence Definition of "Done"

> A user can create a league, add players to it, run through an auction draft
> where each candidate is bid on in turn, see who wins each candidate and how
> their budget updates, and end with every player's final roster.

**Explicitly out of scope for "done":**
- Nominee-matching rules (e.g., requiring a Dem pick + a GOP pick per roster)
- Scoring/winning the fantasy league based on the real-world election outcome
  (can't be resolved until the 2028 election actually happens)

## Step 2: Must-Have vs. Nice-to-Have

### Must-Have (smallest version that satisfies the "done" sentence)
- Create a league, add players
- Load candidate data (placeholder/dummy prices, party label: D, R, or I)
- Cycle through candidates one at a time
- Accept bids with validation (can't exceed remaining budget, can't bid below
  current price, etc.)
- Determine winning bid, assign candidate to winner's roster, update budget
- Save final results (rosters + budgets) to a file at the end of the draft
- Display each player's final roster at the end

### Nice-to-Have (deferred — not required for v1)
- Real prediction-market prices (Kalshi/Polymarket API), swapped in after
  core game logic works
- Scheduling a draft for a future time
- Mid-draft save/resume (continuous saving, not just save-at-end)
- Nominee-matching rules / scoring against the real-world election outcome
- Multi-league support, web UI, historical tracking (from original plan doc)

## Step 3: Nouns (Data Entities)

- **League** — the container for a set of players and available candidates
- **Player** — someone participating who will be drafting candidates, using their budget, etc.
  - Name
  - Budget total
  - Budget remaining (calculated field after candidate is awarded)
- **Candidate** — the political candidates being drafted
  - Name
  - Party
  - Starting price
  - Current price (max of all amounts bid; same as starting price if no bids placed)
- **Roster** — a player's collection of won candidates
  - Team name
  - List of candidates
- **Bid** — a single bid action during the auction
  - Player
  - Candidate
  - Amount bid
- **Draft** — system that lists candidates and their starting prices, and allows all players to bid. Turn-based bidding; everyone must pass before the candidate is awarded. Must give all players at least 1 chance to bid. If all pass, candidate is not rostered. After any player makes a bid, all players must pass. If another bid is made, restart the loop until all the rest have passed. A pass only applies to the current price level; a player can re-enter bidding on a later round for the same candidate

## Step 4: Verbs (Actions/Functions)

### Setup
- Create a league
- Add players to a league
- Load candidate data
- Initiate auction draft

### Loop (per candidate)
- Cycle through candidates
- Player places a bid → validate bid → record bid
- Check if bidding round is over (has everyone but the last bidder passed?)
- Close out bidding on a candidate (determine winner, assign to roster, update budget) or mark candidate unsold
- Check if draft is over (all candidates offered, and/or all players out of budget — your call above)

### Wrap-up
- Save and display final results

---
*Next step: Step 5 — hand-trace a full draft round on paper to pressure-test
the Draft loop logic (tie bids, insufficient budget, invalid input, all-pass
scenarios).*

## Step 5: Trace
Scenario 1:
2 players (minimum amount or players) P1, P2
$100 budget (the default)
JD Vance ($50), AOC ($40), Marco Rubio ($25)
Admin initiates the draft
Candidates are presented in order of starting cost
Bidding order is randomized at the start of each candidate
First player bids 52 on vance
Second player passes
First player is awarded vance
First player has 48 remaining
AOC is up
First player passes
Second player bids 42
First player bids 43
Second bids 44
First passes
AOC is awarded to second player
P2 has 56 remaining
Rubio is up
First bids 26
Second bids 49
First is auto passed (not enough budget)
Rubio goes to second
Draft ends
Players can see their rosters


