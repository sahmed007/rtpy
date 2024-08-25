from .vector import Vec3


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3) -> None:
        self.origin = origin
        self.direction = direction

    def origin(self) -> Vec3:
        return self.origin

    def direction(self) -> Vec3:
        return self.direction

    def at(self, t: float) -> Vec3:
        return self.origin + self.direction * t
