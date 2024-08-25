from typing import List
from rtpy.hittable import Hittable, HitRecord
from rtpy.ray import Ray
from rtpy.interval import Interval


class HittableList(Hittable):
    def __init__(self, object: Hittable = None):
        self.objects: List[Hittable] = []
        if object is not None:
            self.add(object)

    def clear(self) -> None:
        self.objects.clear()

    def add(self, object: Hittable) -> None:
        self.objects.append(object)

    def hit(self, r: Ray, ray_t: Interval, rec: HitRecord) -> bool:
        hit_anything = False
        closest_so_far = ray_t.max

        for object in self.objects:
            temp_rec = HitRecord()
            if object.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.t = temp_rec.t
                rec.front_face = temp_rec.front_face

        return hit_anything
