def rotation(image, factor, is_grayscale=False):
    if not is_grayscale:
        output = image.rotate(factor, fillcolor=(240, 240, 240), expand=True)
    else:
        output = image.rotate(factor, fillcolor=(240), expand=True)
    return output