# import sys
# sys.path.insert(0, '..')
import game


def test_init():
    game.Game()
    # Should not throw


def test_what_what_in_the_board():
    B = game.Board('herpderper')
    print B
    # Should not throw

