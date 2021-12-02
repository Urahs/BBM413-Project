from PIL import ImageEnhance

def brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    output = enhancer.enhance(factor/50)
    return output