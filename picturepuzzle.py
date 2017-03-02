""" This file takes an image and identifies the three most common colors and
then creates a computational art piece with those three colors.

by MJ-McMillen
 """

import random
import math
import colorsys
from PIL import Image
import cmath
from inspect import signature
import MJ_recursive_art_complex as Art

def get_three_colors():
    testimage = Image.open("kitty.jpg")
