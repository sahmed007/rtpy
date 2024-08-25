from rtpy.ray import Ray
from rtpy.vector import Vec3, Point3
from abc import ABC, abstractmethod


class HitRecord:
    def __init__(self, p: Point3, normal: Vec3, t: float):
        self.p: Point3 = p
        self.normal: Vec3 = normal
        self.t: float = t


class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        pass
