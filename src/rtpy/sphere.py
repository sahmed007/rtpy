from rtpy.hittable import Hittable, HitRecord
from rtpy.vector import Point3, vec3_sub, vec3_scalar_mul, dot
from rtpy.ray import Ray
from rtpy.interval import Interval
import math


class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        oc = vec3_sub(r.origin(), self.center)
        a = r.direction().length_squared()
        half_b = dot(oc, r.direction())
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrtd) / a
            if not ray_t.surrounds(root):
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = vec3_scalar_mul(1 / self.radius, vec3_sub(rec.p, self.center))
        rec.set_face_normal(r, outward_normal)

        return True
