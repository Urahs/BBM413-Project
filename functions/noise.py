from PIL import Image, ImageEnhance
import numpy as np
from skimage.util import random_noise

def noise(image, factor, noise_type):
    
    image = np.array(image)

    if noise_type == 1:
        noise_img = random_noise(image, mode='gaussian', var=(factor*0.05)/100)
    elif noise_type == 2:
        noise_img = random_noise(image, mode='speckle', var=(factor*0.05)/100)
    elif noise_type == 3:
        noise_img = random_noise(image, mode='s&p', amount=(factor*0.2)/100)
        
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    
    output = Image.fromarray(noise_img)
    return output