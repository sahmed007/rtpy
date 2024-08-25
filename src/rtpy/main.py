from rtpy.color import Color, write_color
import sys


def main():
    # Image

    image_width = 256
    image_height = 256

    # Render

    print(f"P3\n{image_width} {image_height}\n255")

    for j in range(image_height):
        print(f"\rScanlines remaining: {j}", file=sys.stderr, flush=True)

        for i in range(image_width):
            pixel_color = Color(
                float(i) / (image_width - 1), float(j) / (image_height - 1), 0
            )
            write_color(pixel_color)

    print("\nDone.", file=sys.stderr)


if __name__ == "__main__":
    main()
