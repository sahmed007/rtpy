import math
import random


def degrees_to_radians(degrees: float) -> float:
    return degrees * math.pi / 180.0


def random_float(min: float, max: float) -> float:
    return min + (max - min) * random.random()


def random_float() -> float:
    return random.random()
