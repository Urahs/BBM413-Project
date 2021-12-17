# input comes like this (x1, x2, y1, y2)
def crop(image, inputs):

    for i in range(len(inputs)):
      inputs[i] = int(inputs[i])

    width, height = image.size
    x1 = width*inputs[0]/100
    x2 = width - (width*inputs[1]/100)
    y1 = height*inputs[2]/100
    y2 = height - (height*inputs[3]/100)

    area = (x1, y1, x2, y2)
    output = image.crop(area)
    return output