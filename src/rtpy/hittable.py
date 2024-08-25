from rtpy.ray import Ray
from rtpy.vector import Vec3, Point3, dot
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class HitRecord:
    p: Point3 = field(default_factory=Point3)
    normal: Vec3 = field(default_factory=Vec3)
    t: float = 0.0
    front_face: bool = False

    def set_face_normal(self, r: Ray, outward_normal: Vec3):
        self.front_face = dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        pass
