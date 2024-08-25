from rtpy import *
import sys
import math


def hit_sphere(center: Point3, radius: float, r: Ray) -> float:
    oc = vec3_sub(r.origin(), center)
    a = r.direction().length_squared()
    h = dot(r.direction(), oc)
    c = oc.length_squared() - radius * radius
    discriminant = h * h - a * c

    if discriminant < 0:
        return -1.0
    else:
        return (-h - math.sqrt(discriminant)) / a


def ray_color(r: Ray, world: Hittable) -> Color:
    rec = HitRecord()
    if world.hit(r, Interval(0.0, math.inf), rec):
        return vec3_scalar_mul(0.5, vec3_add(rec.normal, Color(1, 1, 1)))

    unit_direction = unit_vector(r.direction())
    a = 0.5 * (unit_direction.y() + 1.0)
    return vec3_add(
        vec3_scalar_mul(1.0 - a, Color(1.0, 1.0, 1.0)),
        vec3_scalar_mul(a, Color(0.5, 0.7, 1.0)),
    )


def main():
    # Image

    aspect_ratio = 16.0 / 9.0
    image_width = 400

    # Calculate the image height, ensuring it is at least 1
    image_height: int = int(image_width / aspect_ratio)
    image_height: int = max(1, image_height)

    # World

    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # Camera

    focal_length: float = 1.0
    viewport_height: float = 2.0
    viewport_width: float = viewport_height * (float(image_width) / image_height)
    camera_center: Point3 = Point3(0, 0, 0)

    # Calculate the vectors across the horizontal and down the vertical viewport edges
    viewport_u: Vec3 = Vec3(viewport_width, 0, 0)
    viewport_v: Vec3 = Vec3(0, -viewport_height, 0)

    # Calculate the horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u: Vec3 = vec3_div(viewport_u, image_width)
    pixel_delta_v: Vec3 = vec3_div(viewport_v, image_height)

    # Calculate the location of the upper left pixel
    viewport_upper_left: Vec3 = vec3_sub(
        camera_center,
        vec3_add(
            Vec3(0, 0, focal_length),
            vec3_add(vec3_div(viewport_u, 2), vec3_div(viewport_v, 2)),
        ),
    )
    pixel00_loc: Vec3 = vec3_add(
        viewport_upper_left,
        vec3_scalar_mul(0.5, vec3_add(pixel_delta_u, pixel_delta_v)),
    )

    # Render

    print(f"P3\n{image_width} {image_height}\n255")

    for j in range(image_height):
        print(f"\rScanlines remaining: {j}", file=sys.stderr, flush=True)

        for i in range(image_width):
            pixel_center: Vec3 = vec3_add(
                pixel00_loc,
                vec3_add(
                    vec3_scalar_mul(i, pixel_delta_u),
                    vec3_scalar_mul(j, pixel_delta_v),
                ),
            )
            ray_direction: Vec3 = vec3_sub(pixel_center, camera_center)
            pixel_color: Color = ray_color(Ray(camera_center, ray_direction), world)
            write_color(pixel_color)

    print("\nDone.", file=sys.stderr)


if __name__ == "__main__":
    main()
