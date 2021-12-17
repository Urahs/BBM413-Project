from PIL import ImageChops

def reverse_color(image):
    image = ImageChops.invert(image)
    return image