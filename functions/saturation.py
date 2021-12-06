from PIL import ImageEnhance

def saturation(image, factor):
    enhancer = ImageEnhance.Color(image)
    output = enhancer.enhance((factor*3)/100)
    return output