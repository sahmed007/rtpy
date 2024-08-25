from rtpy.ray import Ray
from rtpy.hittable import Hittable, HitRecord
from rtpy.interval import Interval
from rtpy.color import Color, write_color
from rtpy.vector import Vec3, Point3, vec3_add, vec3_sub, vec3_scalar_mul, unit_vector
import math
import sys


class Camera:
    def __init__(self, aspect_ratio: float = 16.0 / 9.0, image_width: int = 400):
        self.aspect_ratio: float = aspect_ratio
        self.image_width: int = image_width
        self.image_height: int = max(1, int(image_width / aspect_ratio))

        self.center: Vec3 = Point3(0, 0, 0)
        self.focal_length: float = 1.0
        self.viewport_height: float = 2.0
        self.viewport_width: float = self.viewport_height * (
            float(self.image_width) / self.image_height
        )

        self.initialize()

    def initialize(self):
        # Calculate the vectors across the horizontal and down the vertical viewport edges
        viewport_u: Vec3 = Vec3(self.viewport_width, 0, 0)
        viewport_v: Vec3 = Vec3(0, -self.viewport_height, 0)

        # Calculate the horizontal and vertical delta vectors from pixel to pixel
        self.pixel_delta_u: Vec3 = vec3_scalar_mul(1.0 / self.image_width, viewport_u)
        self.pixel_delta_v: Vec3 = vec3_scalar_mul(1.0 / self.image_height, viewport_v)

        # Calculate the location of the upper left pixel
        viewport_upper_left: Vec3 = vec3_sub(
            vec3_sub(
                vec3_sub(self.center, Vec3(0, 0, self.focal_length)),
                vec3_scalar_mul(0.5, viewport_u),
            ),
            vec3_scalar_mul(0.5, viewport_v),
        )
        self.pixel00_loc: Vec3 = vec3_add(
            viewport_upper_left,
            vec3_scalar_mul(0.5, vec3_add(self.pixel_delta_u, self.pixel_delta_v)),
        )

    def render(self, world: Hittable):
        self.initialize()

        print(f"P3\n{self.image_width} {self.image_height}\n255")

        for j in range(self.image_height):
            print(
                f"\rScanlines remaining: {self.image_height - j} ",
                end="",
                file=sys.stderr,
                flush=True,
            )
            for i in range(self.image_width):
                pixel_center = vec3_add(
                    self.pixel00_loc,
                    vec3_add(
                        vec3_scalar_mul(i, self.pixel_delta_u),
                        vec3_scalar_mul(j, self.pixel_delta_v),
                    ),
                )
                ray_direction = vec3_sub(pixel_center, self.center)
                r = Ray(self.center, ray_direction)

                pixel_color = self.__ray_color(r, world)
                write_color(pixel_color)

        print("\rDone.                 ", file=sys.stderr)

    def __ray_color(self, r: Ray, world: Hittable):
        rec: HitRecord = HitRecord()

        if world.hit(r, Interval(0, math.inf), rec):
            return vec3_scalar_mul(0.5, vec3_add(rec.normal, Color(1, 1, 1)))

        unit_direction: Vec3 = unit_vector(r.direction())
        a: float = 0.5 * (unit_direction.y() + 1.0)
        return vec3_add(
            vec3_scalar_mul(1.0 - a, Color(1.0, 1.0, 1.0)),
            vec3_scalar_mul(a, Color(0.5, 0.7, 1.0)),
        )
