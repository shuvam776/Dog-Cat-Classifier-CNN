from PIL import Image
import numpy as np
IMAGE_SIZE = (224,224)

MEAN = np.array([0.485,0.456,0.406],dtype=np.float32)
STD = np.array([0.229,0.224,0.225],dtype=np.float32)

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(IMAGE_SIZE)
    image = np.array(image).astype(np.float32)
    image /= 255.0
    image = (image - MEAN)/STD
    image = np.transpose(image,(2,0,1))
    image = np.expand_dims(image,axis=0)
    return image.astype(np.float32)