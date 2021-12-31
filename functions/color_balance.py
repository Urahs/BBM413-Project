from PIL import Image

def color_balance(image, R, G, B):
  imageR, imageG, imageB = image.split()
  imageR = imageR.point(lambda i: (255 // (255 - R)) * i)
  imageG = imageG.point(lambda i: (255 // (255 - G)) * i)
  imageB = imageB.point(lambda i: (255 // (255 - B)) * i)
  return Image.merge('RGB', (imageR, imageG, imageB))