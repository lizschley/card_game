'''
     driver for card game

     Usage
     >>> python game_driver.py name_1 name_2
    Note - must have > one name listed after file name
'''
from game_classes.card_game import CardGame

import sys


if __name__ == "__main__":
    args_count = len(sys.argv)
    if args_count < 3:
        sys.exit(f'Must have at least two name following program filename: {sys.argv}')
    players = []
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        players.append(arg)
    game = CardGame(players)
    game.play_game()
