from .vector import Vec3
from .interval import Interval
import math

# Define Color as an alias for Vec3
Color = Vec3


def linear_to_gamma(linear_component: float) -> float:
    if linear_component > 0.0:
        return math.sqrt(linear_component)
    return 0.0


def write_color(pixel_color: Color) -> None:
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Apply gamma correction
    r = linear_to_gamma(r)
    g = linear_to_gamma(g)
    b = linear_to_gamma(b)

    # Translate the [0, 1] component values to the byte range [0, 255]
    intensity = Interval(0.0, 0.999)
    rbyte = int(255.999 * intensity.clamp(r))
    gbyte = int(255.999 * intensity.clamp(g))
    bbyte = int(255.999 * intensity.clamp(b))

    # Write out the pixel color components
    print(f"{rbyte} {gbyte} {bbyte}")
