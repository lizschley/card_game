COLOR_VALUES = {'red': 3,
                'orange': 4,
                'yellow': 2,
                'green': 1,
                'blue': 5,
                'indigo': 6,
                'violet': 7}


class Card:
    ''' One card used in card game'''
    def __init__(self, color, card_value, color_sort=0):
        '''
        __init__ initializes the cards

        :param color: color name for the card
        :type color: string
        :param card_value: number that is past in; controlled by the game
        :type card_value: int
        :param color_sort: this can be changed, based on the input array when sorting, defaults to 0
        :type color_sort: int, optional
        '''
        self.color_name = color
        self.color_value = COLOR_VALUES.get(color, 8)
        self.card_value = card_value
        self.color_sort = color_sort

    def __eq__(self, other_card):
        '''
        __eq__ used for sorting

        :param other_card: card that is being compared against
        :type other_card: Card
        '''
        self.color_sort == other_card.color_sort and self.card_value == other_card.card_value

    def __lt__(self, other_card):
        '''
        __lt__ used for sorting

        :param other_card: card that is being compared against
        :type other_card: Card
        '''
        if self.color_sort < other_card.color_sort:
            return True
        return self.card_value < other_card.card_value

    def __str__(self):
        '''
        __str__ used so that the card can be printed out as part of taking a turn

        :return: string describing the Card
        :rtype: string
        '''
        return (f'Card --> color_name: {self.color_name}, '
                f'color value: {self.color_value}, '
                f'card value: {self.card_value}, '
                f'card sort: {self.color_sort}, '
                f'total_value: {self.color_value * self.card_value}')

    def total_value(self):
        '''
        total_value returns the value of the Card

        :return: color_value * card_value
        :rtype: int
        '''
        return self.color_value * self.card_value

    def assign_new_color_sort(self, num):
        '''
        assign_new_color_sort, this will be the primary sort which is based on color

        :param num: sort order of colors
        :type num: int
        '''
        self.color_sort = num
