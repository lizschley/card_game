import pytest
from game_classes.card_game import CardGame


@pytest.fixture(scope='session')
def sort_colors():
    return [['red', 'yellow', 'green'],
            ['green', 'red', 'yellow'],
            ['yellow', 'red', 'green']]


@pytest.fixture()
def card_game():
    return CardGame(['Ninja', 'Ronin'])

