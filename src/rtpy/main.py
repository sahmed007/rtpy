def main():
    # Image

    image_width = 256
    image_height = 256

    # Render

    print(f"P3\n{image_width} {image_height}\n255")

    for j in range(image_height):
        print(f"\rScanlines remaining: {image_height - j}")

        for i in range(image_width):
            r = i / (image_width - 1)
            g = j / (image_height - 1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f"{ir} {ig} {ib}")

    print("\nDone.")


if __name__ == "__main__":
    main()
