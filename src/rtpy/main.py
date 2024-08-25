from rtpy import *


def main():
    # World
    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # Camera
    camera = Camera()
    camera.aspect_ratio = 16.0 / 9.0
    camera.image_width = 400
    camera.samples_per_pixel = 100

    camera.render(world)


if __name__ == "__main__":
    main()
