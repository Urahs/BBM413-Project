from PIL import ImageEnhance

def sharpness(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    output = enhancer.enhance((factor+25)/25)
    return output