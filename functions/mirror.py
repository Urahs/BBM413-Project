from PIL import ImageOps

def mirror(image):
    image = ImageOps.mirror(image)
    return image