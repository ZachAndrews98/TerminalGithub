""" Utilities for user interactions and experience. """

import os

from bullet import Input
from bullet import ScrollBar
from bullet import YesNo


def option_select(prompt="", choices=None):
    """ Bullet option select utility. """
    return ScrollBar(
        prompt=prompt,
        choices=choices,
        margin=2,
        pointer="→"
    ).launch()


def get_input(prompt="", strip=False):
    """ Bullet input handling utility. """
    return Input(
        prompt=prompt,
        strip=strip
    ).launch()


def get_yes_no(prompt=""):
    """ Bullet y/n input handling utility. """
    return YesNo(
        prompt=prompt
    ).launch()


def cls():
    """ Clear the terminal. """
    os.system('cls' if os.name == 'nt' else 'clear')
