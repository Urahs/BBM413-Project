from PIL import ImageChops

def is_grayscale(image):
    if image.mode not in ("L", "RGB"):
        raise ValueError("Unsuported image mode")

    if image.mode == "RGB":
        rgb = image.split()
        if ImageChops.difference(rgb[0],rgb[1]).getextrema()[1]!=0: 
            return False
        if ImageChops.difference(rgb[0],rgb[2]).getextrema()[1]!=0: 
            return False
    return True