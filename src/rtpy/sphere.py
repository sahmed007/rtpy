from rtpy.hittable import Hittable, HitRecord
from rtpy.ray import Ray
from rtpy.vector import Vec3, Point3, vec3_sub, dot
import math


class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float):
        self.center: Point3 = center
        self.radius: float = max(0, radius)

    def hit(self, r: Ray, ray_tmin: float, ray_tmax: float, rec: HitRecord) -> bool:
        oc: Vec3 = vec3_sub(self.center, r.origin())
        a = r.direction().length_squared()
        h = dot(r.direction(), oc)
        c = oc.length_squared() - self.radius * self.radius
        
        discriminant = h * h - a * c
        if discriminant < 0:
            return False
        
        sqrtd: float = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range
        root: float = (h - sqrtd) / a
        if root < ray_tmin or root > ray_tmax:
            root = (h + sqrtd) / a
            if root < ray_tmin or root > ray_tmax:
                return False
        
        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal: Vec3 = vec3_sub(rec.p, self.center) / self.radius
        return True
