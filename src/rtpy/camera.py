from rtpy.ray import Ray
from rtpy.hittable import Hittable, HitRecord
from rtpy.interval import Interval
from rtpy.color import Color, write_color
from rtpy.vector import (
    Vec3,
    Point3,
    vec3_add,
    vec3_sub,
    vec3_scalar_mul,
    unit_vector,
    random_on_hemisphere,
)
import math
import sys
import random


class Camera:
    ASPECT_RATIO = 1.0
    IMAGE_WIDTH = 100
    SAMPLES_PER_PIXEL = 10
    MAX_DEPTH = 10

    def __init__(self):
        self._aspect_ratio = self.ASPECT_RATIO
        self._image_width = self.IMAGE_WIDTH
        self._samples_per_pixel = self.SAMPLES_PER_PIXEL
        self.center = Point3(0, 0, 0)
        self.initialize()

    @property
    def aspect_ratio(self):
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, value):
        self._aspect_ratio = value
        self.initialize()

    @property
    def image_width(self):
        return self._image_width

    @image_width.setter
    def image_width(self, value):
        self._image_width = value
        self.initialize()

    @property
    def samples_per_pixel(self):
        return self._samples_per_pixel

    @samples_per_pixel.setter
    def samples_per_pixel(self, value):
        self._samples_per_pixel = value
        self.initialize()

    def initialize(self):
        self.image_height = max(1, int(self._image_width / self._aspect_ratio))
        self.pixel_samples_scale = 1.0 / self._samples_per_pixel

        # Calculate the viewport dimensions
        self.focal_length = 1.0
        self.viewport_height = 2.0
        self.viewport_width = self.viewport_height * (
            self._image_width / self.image_height
        )

        # Calculate the vectors across the horizontal and down the vertical viewport edges
        viewport_u = Vec3(self.viewport_width, 0, 0)
        viewport_v = Vec3(0, -self.viewport_height, 0)

        # Calculate the horizontal and vertical delta vectors from pixel to pixel
        self.pixel_delta_u = vec3_scalar_mul(1.0 / self._image_width, viewport_u)
        self.pixel_delta_v = vec3_scalar_mul(1.0 / self.image_height, viewport_v)

        # Calculate the location of the upper left pixel
        viewport_upper_left = vec3_sub(
            vec3_sub(
                vec3_sub(self.center, Vec3(0, 0, self.focal_length)),
                vec3_scalar_mul(0.5, viewport_u),
            ),
            vec3_scalar_mul(0.5, viewport_v),
        )
        self.pixel00_loc = vec3_add(
            viewport_upper_left,
            vec3_scalar_mul(0.5, vec3_add(self.pixel_delta_u, self.pixel_delta_v)),
        )

    def get_ray(self, i: int, j: int) -> Ray:
        # Construct a camera ray originating from the origin and directed at randomly sampled
        # point around the pixel location i, j.
        offset = self.sample_square()
        pixel_sample = vec3_add(
            self.pixel00_loc,
            vec3_add(
                vec3_scalar_mul(i + offset.x(), self.pixel_delta_u),
                vec3_scalar_mul(j + offset.y(), self.pixel_delta_v),
            ),
        )

        ray_origin = self.center
        ray_direction = vec3_sub(pixel_sample, ray_origin)

        return Ray(ray_origin, ray_direction)

    def sample_square(self) -> Vec3:
        # Returns the vector to a random point in the [-.5,-.5]-[+.5,+.5] unit square.
        return Vec3(random.random() - 0.5, random.random() - 0.5, 0)

    def render(self, world: Hittable):
        self.initialize()

        print(f"P3\n{self._image_width} {self.image_height}\n255")

        for j in range(self.image_height):
            print(
                f"\rScanlines remaining: {self.image_height - j} ",
                end="",
                file=sys.stderr,
                flush=True,
            )
            for i in range(self._image_width):
                pixel_color = Color(0, 0, 0)
                for _ in range(self._samples_per_pixel):
                    r = self.get_ray(i, j)
                    # pixel_color = vec3_add(pixel_color, self.__ray_color(r, world))
                    pixel_color += self.__ray_color(r, self.MAX_DEPTH, world)

                pixel_color = vec3_scalar_mul(self.pixel_samples_scale, pixel_color)
                write_color(pixel_color)

        print("\rDone.                 ", file=sys.stderr)

    def __ray_color(self, r: Ray, depth: int, world: Hittable):
        # If we've exceeded the ray bounce limit, no more light is gathered
        if depth <= 0:
            return Color(0, 0, 0)

        rec: HitRecord = HitRecord()

        if world.hit(r, Interval(0, math.inf), rec):
            direction: Vec3 = random_on_hemisphere(rec.normal)
            return vec3_scalar_mul(
                0.5, self.__ray_color(Ray(rec.p, direction), depth - 1, world)
            )

        unit_direction: Vec3 = unit_vector(r.direction())
        a: float = 0.5 * (unit_direction.y() + 1.0)
        return vec3_add(
            vec3_scalar_mul(1.0 - a, Color(1.0, 1.0, 1.0)),
            vec3_scalar_mul(a, Color(0.5, 0.7, 1.0)),
        )
