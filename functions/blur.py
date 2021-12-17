from PIL import ImageFilter

def blur(image, factor, blur_type):
  
  if blur_type == 1:
    output = image.filter(ImageFilter.GaussianBlur(factor))
  else:
    output = image.filter(ImageFilter.BoxBlur(factor))

  return output