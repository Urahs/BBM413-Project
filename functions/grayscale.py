from PIL import Image, ImageOps
def grayscale(image):
  image = ImageOps.grayscale(image)
  return image