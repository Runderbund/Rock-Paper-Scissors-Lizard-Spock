# 10 Commits
    # Every time we make a function/class or modify
# Use inheritance
    # Human and AI inherit from Player
# Check user input, re-ask
    # Use @ on these?
# Store choices as List of Strings
# Correctly choose winner
# Game is best of 3
    # Could give options as extra
# Have option for single (human vs PC) or multiplayer (human vs human)
    # I was assuming more than one player. Doesn't sound like it.
        # Maybe give option. Would complicate it.

"""
Start creating classes. Start thinking through what every class “has” and “does” based on the user stories and instructor discussion.
"""

"""
Before you begin coding, write an algorithm that represents the steps necessary to play a game of rock, paper, scissors, lizard, Spock in a best-of-three format. By writing out the steps, it will make you think about every piece needed to bring the game to life. Please submit to your instructor Slack channel once completed for approval to start coding. Below is an example of how to get started: 
Step 1: Display the rules of the game 
Step 2: Ask how many human players will be playing 
… etc
"""

"""
Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
"""

# Demo uses sleep function to display slowly.
    # And play again prompt.
# main.pyt has
# from game import Game
# if __name__ == '__main__':
#     game = Game()
#     game.run_game()

"""
Steps:
1. Display Rules
2. Ask whether 1 or 2 players.
3. Get gesture for each player.
    - input() for human
    - random.randint(0,4) for AI
4. Compare choices and determine winner
5. Increment counter for wins
    - As part of game.py or
    - As an attribute of the player.
6. Loop game until counter = 2
7. Print winner
    - Ask whether to play again

Player class
- Initialize with score = 0
- Have choose gesture method?
    - Going to be different in human/AI, so no need?
"""