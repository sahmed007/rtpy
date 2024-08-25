from rtpy.hittable import Hittable, HitRecord
from rtpy.ray import Ray
from rtpy.vector import Vec3, Point3, dot
import math


class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float):
        self.center: Point3 = center
        self.radius: float = max(0, radius)

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        oc: Vec3 = r.origin() - self.center  # Changed order of subtraction
        a = r.direction().length_squared()
        h = dot(r.direction(), oc)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = h * h - a * c
        if discriminant < 0:
            return False

        sqrtd: float = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range
        root: float = (h - sqrtd) / a
        if root <= ray_tmin or ray_tmax <= root:  # Changed condition
            root = (h + sqrtd) / a
            if root <= ray_tmin or ray_tmax <= root:  # Changed condition
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        return True
