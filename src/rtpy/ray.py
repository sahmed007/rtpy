from .vector import Vec3, vec3_add, vec3_scalar_mul


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3) -> None:
        self._origin = origin
        self._direction = direction

    def origin(self) -> Vec3:
        return self._origin

    def direction(self) -> Vec3:
        return self._direction

    def at(self, t: float) -> Vec3:
        return vec3_add(self._origin, vec3_scalar_mul(t, self._direction))
