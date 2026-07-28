import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR,"models","resnet50.onnx")

UPLOAD_FOLDER = os.path.join(BASE_DIR,"static","uploads")

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "webp"
}
IMAGE_SIZE = (224,244)
CLASS_NAMES = {
    0: "Cat",
    1: "Dog"
}