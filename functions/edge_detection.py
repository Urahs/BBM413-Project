from PIL import ImageFilter

def edge_detection(image):
  image = image.filter(ImageFilter.FIND_EDGES)
  return image