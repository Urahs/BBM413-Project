from PIL import ImageOps

def grayscale(image):
  image = ImageOps.grayscale(image)
  return image