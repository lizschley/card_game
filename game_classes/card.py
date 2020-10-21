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
        self.color_name = color
        self.color_value = COLOR_VALUES.get(color, 8)
        self.card_value = card_value
        self.color_sort = color_sort

    def __eq__(self, other_card):
        self.color_sort == other_card.color_sort and self.card_value == other_card.card_value

    def __lt__(self, other_card):
        if self.color_sort < other_card.color_sort:
            return True
        return self.card_value < other_card.card_value

    def __str__(self):
        return (f'Card --> color_name: {self.color_name}, '
                f'color value: {self.color_value}, '
                f'card value: {self.card_value}, '
                f'card sort: {self.color_sort}, '
                f'total_value: {self.color_value * self.card_value}')

    def total_value(self):
        return self.color_value * self.card_value

    def assign_new_color_sort(self, num):
        self.color_sort = num
