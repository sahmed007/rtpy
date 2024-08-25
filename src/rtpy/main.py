from rtpy import *


def main():
    # World
    world = HittableList()
    world.add(Sphere(Point3(0, 0, -1), 0.5))
    world.add(Sphere(Point3(0, -100.5, -1), 100))

    # Camera
    camera = Camera()
    camera.render(world)


if __name__ == "__main__":
    main()
