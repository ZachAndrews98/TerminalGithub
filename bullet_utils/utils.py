import os

from bullet import Bullet
from bullet import Input
from bullet import Password
from bullet import YesNo
from bullet import colors
from bullet import ScrollBar

# STYLE = {
#     "bullet": "→"
#     # "bullet_color" : colors.foreground["white"],
#     # "word_color" : colors.foreground["blue"],
#     # "word_on_switch" : colors.foreground["white"],
#     # "background_color" : colors.background["white"],
#     # "background_on_switch" : colors.background["blue"]
# }


def option_select(prompt="", choices=[]):
    return ScrollBar(
        prompt=prompt,
        choices=choices,
        margin=2,
        pointer="→"
        # **STYLE
    ).launch()


def get_input(prompt="", strip=False):
    return Input(
        prompt=prompt,
        strip=strip,
        margin=2,
    ).launch()


def get_password(prompt=""):
    return Password(
        prompt=prompt,
        hidden="*",
        margin=2,
    ).launch()


def get_YesNo(prompt=""):
    return YesNo(
        prompt=prompt
    ).launch()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
