import io
from PIL import Image


def main():
    with open("/usr/src/data.txt", "rb") as img_bytes:
        img_bytes = img_bytes.read()
        with Image.open(io.BytesIO(img_bytes)) as img:
            img.save("/usr/src/output/img.jpg")


if __name__ == "__main__":
    main()
