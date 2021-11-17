from PIL import ImageOps

def flip(image):
    image = ImageOps.flip(image)
    return image