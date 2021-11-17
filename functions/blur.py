from PIL import ImageFilter
def blur(image):
  image = image.filter(ImageFilter.BLUR)
  return image