from PIL import ImageFilter

def blur(image, factor, blur_type):
  if blur_type == 1:
    output = image.filter(ImageFilter.GaussianBlur(factor/10))
  else:
    output = image.filter(ImageFilter.BoxBlur(factor/10))
  return output