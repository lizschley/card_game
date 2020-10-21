
import operator
import pprint
import random
from game_classes.card import Card


class CardGame:

    DEFAULT_COLORS = ['yellow', 'green', 'red']

    def __init__(self, players):
        '''
        __init__ for CardGame

        sets the process data for the game

        :param players: list of player names
        :type players: list
        '''
        self.players = players
        self.last_player = players[-1]
        self.score_sheet = {}
        self.turn_idx = 0
        self.deck = []
        self.colors_used = None
        self.num_turns = 0
        for player in players:
            self.score_sheet[player] = 0

    def __call__(self, players):
        self.__init__(players)

    def play_game(self):
        '''
        play_game driver to play the game
        '''
        self.make_card_deck()
        self.shuffle_deck()
        self.game_loop()

    def game_loop(self):
        '''
        game_loop players take turns getting cards and adding them to their score
        1. Can end by user request
        2. Can end when the cards when there are not enough cards for each player to get one
        '''
        while len(self.deck) > 0:
            stop = self.time_to_stop()
            if stop:
                self.end_game()
                break
            if self.user_stop_request():
                self.end_game()
                break
            player = self.players[self.turn_idx]
            card_played = self.take_turn(player)
            if not card_played:
                self.end_game()
                break
            else:
                print(f'{player}\'s {card_played}')
                print(' ')

    def user_stop_request(self):
        '''
        user_stop_request if the user enters q or Q as the first or only letter, game stops

        :return: True if the user enters q or Q, otherwise return False
        :rtype: bool
        '''
        self.print_message(self.turn_message())
        reply = input()
        try:
            if reply.lower()[0] == 'q':
                return True
        except IndexError:
            return False

    def end_game(self):
        '''
        end_game when the game ends, a winner is determined

        [extended_summary]
        '''
        self.print_message(self.results_message())
        self.deck = []

    def make_card_deck(self, colors=DEFAULT_COLORS, num_per_color=3):
        self.colors_used = colors
        new_deck = []
        nums = range(1, num_per_color + 1)
        for card_num in nums:
            for color_sort, color_name in enumerate(colors):
                new_deck.append(Card(color_name, card_num, color_sort))
        self.deck = new_deck

    def sort_deck(self, colors=DEFAULT_COLORS):
        self.assign_color_sort(colors)
        self.deck.sort()

    def assign_color_sort(self, colors):
        message = self.check_for_discrepency(colors)
        if message:
            self.print_message(message, False)

        for card in self.deck:
            if card.color_name in colors:
                card.assign_new_color_sort(colors.index(card.color_name))
            else:
                card.assign_new_color_sort(2000)

    def check_for_discrepency(self, colors):
        msg = []
        all_colors_in_cards = all(item in self.colors_used for item in colors)
        all_card_colors_in_colors = all(item in colors for item in self.colors_used)
        if not all_colors_in_cards:
            msg.append('Passed in colors are not in the cards. Those colors will be ignored. ')
        if not all_card_colors_in_colors:
            msg.append('Cards with colors that are not passed will sort at bottom by card number.')
        if msg:
            msg.append(f'card colors == {self.colors_used}, passed in colors == {colors}')
        return msg

    def time_to_stop(self):
        if not self.equal_turns():
            return True
        if self.num_turns > 0:
            self.next_turn()
        return False

    def equal_turns(self):
        return len(self.deck)//len(self.players)

    def results_message(self):
        return [f'After {self.num_turns} turns, {self.find_winner()} won!!!!']

    def turn_message(self):
        return [f'Take turn number {self.num_turns + 1}, {self.players[self.turn_idx]}.  ',
                'Press "q" or "Q" then <enter> (no quotes) to quit, otherwise just press <enter> ']

    def print_message(self, message, print_scores=True):
        if print_scores:
            print('Current Score Sheet: ')
            printer = pprint.PrettyPrinter(indent=1, width=120)
            printer.pprint(self.score_sheet)
            print(' ')
        for msg in message:
            print(msg)

    def find_winner(self):
        max_value = max(self.score_sheet.values())
        max_list = [k for k, v in self.score_sheet.items() if v == max_value]
        if not max_list:
            return max(self.score_sheet.items(), key=operator.itemgetter(1))[0]
        return ' and '.join(max_list)

    def take_turn(self, player):
        try:
            card_to_play = self.deck.pop()
        except IndexError:
            return None
        self.score_sheet[player] += card_to_play.total_value()
        self.num_turns += 1
        return card_to_play

    def next_turn(self):
        max = len(self.players) - 1
        if self.turn_idx == max:
            self.turn_idx = 0
        else:
            self.turn_idx += 1

    def shuffle_deck(self):
        random.shuffle(self.deck)
