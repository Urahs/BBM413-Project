from PIL import ImageEnhance

def contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    output = enhancer.enhance(factor/50)
    return output