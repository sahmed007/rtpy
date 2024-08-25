import math


class Interval:
    def __init__(self, min: float = math.inf, max: float = -math.inf):
        self.min = min
        self.max = max

    def size(self) -> float:
        return self.max - self.min

    def contains(self, x: float) -> bool:
        return self.min <= x and x <= self.max

    def surrounds(self, x: float) -> bool:
        return self.min < x and x < self.max

    def clamp(self, x: float) -> float:
        return max(self.min, min(x, self.max))

    empty = None
    universe = None


Interval.empty = Interval()
Interval.universe = Interval(-math.inf, math.inf)
