import pytest
from game_classes.card_game import CardGame


@pytest.fixture(scope='session')
def sort_colors():
    return [['red', 'yellow', 'green'],
            ['green', 'red', 'yellow'],
            ['yellow', 'red', 'green']]


@pytest.fixture()
def extra_colors(scope='session'):
    return ['chartreuse', 'red', 'yellow', 'green']


@pytest.fixture()
def missing_colors(scope='session'):
    return ['red', 'yellow']


@pytest.fixture()
def card_game():
    return CardGame(['Ninja', 'Ronin'])
