''' Tests for Card class'''
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
import game_classes.card as card


@pytest.mark.parametrize('color, card_value, card_total', [('yellow', 2, 4),
                                                           ('yellow', 8, 16),
                                                           ('green', 1, 1),
                                                           ('green', 6, 6),
                                                           ('red', 5, 15),
                                                           ('red', 7, 21)])
def test_card_total(color, card_value, card_total):
    assert card.COLOR_VALUES[color] * card_value == card_total


@pytest.mark.parametrize('color_idx', [(0), (1), (2)])
def test_cards_sort_by_colors_index_and_card_value(card_game, sort_colors, color_idx):
    color_list = sort_colors[color_idx]
    card_game.make_card_deck()
    card_game.sort_deck(color_list)
    assert sorted_deck_check(color_list, card_game.deck)


def test_shuffle_deck(card_game, sort_colors):
    color_list = sort_colors[0]
    card_game.make_card_deck()
    card_game.sort_deck(color_list)
    card_game.shuffle_deck()
    assert random_deck_check(color_list, card_game.deck)


def sorted_deck_check(sort_order, sorted_deck):
    for sorted_card in sorted_deck:
        print(f'sorted card=={sorted_card}')

    if sorted_deck[0].color_name != sort_order[0]:
        return False
    if sorted_deck[4].color_name != sort_order[1]:
        return False
    if sorted_deck[8].color_name != sort_order[2]:
        return False
    if sorted_deck[0].card_value >= sorted_deck[1].card_value:
        return False
    if sorted_deck[1].card_value >= sorted_deck[2].card_value:
        return False
    return True


def random_deck_check(sort_order, random_deck):
    for random_card in random_deck:
        print(f'random card=={random_card}')
    count = 0
    if (random_deck[0].color_name == sort_order[0] and
            random_deck[1].color_name == sort_order[0] and
            random_deck[2].color_name == sort_order[0] and
            random_deck[3].color_name == sort_order[1] and
            random_deck[4].color_name == sort_order[1] and
            random_deck[5].color_name == sort_order[1] and
            random_deck[6].color_name == sort_order[2] and
            random_deck[7].color_name == sort_order[2] and
            random_deck[8].color_name == sort_order[2]):
        count += 1
    if (random_deck[0].card_value < random_deck[1].card_value and
            random_deck[1].card_value < random_deck[2].card_value and
            random_deck[3].card_value < random_deck[4].card_value and
            random_deck[4].card_value < random_deck[5].card_value and
            random_deck[6].card_value < random_deck[7].card_value and
            random_deck[7].card_value < random_deck[8].card_value):
        count += 1
    return count == 0