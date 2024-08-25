from .vector import Vec3

# Define Color as an alias for Vec3
Color = Vec3


def write_color(pixel_color: Color) -> None:
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Translate the [0, 1] component values to the byte range [0, 255]
    rbyte = int(255.999 * r)
    gbyte = int(255.999 * g)
    bbyte = int(255.999 * b)

    # Write out the pixel color components
    print(f"{rbyte} {gbyte} {bbyte}")
