
def rotation(image, factor):
    output = image.rotate(factor, fillcolor=(240, 240, 240), expand=True)
    return output