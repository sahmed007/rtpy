from __future__ import annotations
import math


class Vec3:
    def __init__(self, e0: float, e1: float, e2: float) -> None:
        self.e = [e0, e1, e2]

    def x(self) -> float:
        return self.e[0]

    def y(self) -> float:
        return self.e[1]

    def z(self) -> float:
        return self.e[2]

    def __neg__(self) -> Vec3:
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, index: int) -> float:
        return self.e[index]

    def __setitem__(self, index: int, value: float) -> None:
        self.e[index] = value

    def __iadd__(self, other: Vec3) -> Vec3:
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __imul__(self, t: float) -> Vec3:
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t: float) -> "Vec3":
        return self.__imul__(1 / t)

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def length_squared(self) -> float:
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2


# Define Point3 as an alias for Vec3
Point3 = Vec3


# Vector Utility functions
def vec3_str(v: Vec3) -> str:
    return f"{v.e[0]} {v.e[1]} {v.e[2]}"


def vec3_add(u: Vec3, v: Vec3) -> Vec3:
    return Vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])


def vec3_sub(u: Vec3, v: Vec3) -> Vec3:
    return Vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2])


def vec3_mul(t: float, v: Vec3) -> Vec3:
    return Vec3(t * v.e[0], t * v.e[1], t * v.e[2])


def vec3_scalar_mul(v: Vec3, t: float) -> Vec3:
    return Vec3(v.e[0] * t, v.e[1] * t, v.e[2] * t)


def vec3_scalar_mul_rev(v: Vec3, t: float) -> Vec3:
    return vec3_scalar_mul(t, v)


def vec3_div(v: Vec3, t: float) -> Vec3:
    return vec3_scalar_mul(1 / t, v)


def dot(u: Vec3, v: Vec3) -> float:
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]


def cross(u: Vec3, v: Vec3) -> Vec3:
    return Vec3(
        u.e[1] * v.e[2] - u.e[2] * v.e[1],
        u.e[2] * v.e[0] - u.e[0] * v.e[2],
        u.e[0] * v.e[1] - u.e[1] * v.e[0],
    )


def unit_vector(v: Vec3) -> Vec3:
    return vec3_div(v, v.length())
