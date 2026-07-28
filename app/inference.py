import time
import numpy as np
try:
    import onnxruntime as ort
except ImportError:
    ort = None
from config import MODEL_PATH
from config import CLASS_NAMES
from preprocess import preprocess_image

class DogCatPredictor:
    def __init__(self):
        if ort is None:
            raise RuntimeError("onnxruntime is not installed. Install it using: pip install onnxruntime")
        self.session = ort.InferenceSession(
            MODEL_PATH,
            providers=["CPUExecutionProvider"]
        )
        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name
    
    def sigmoid(self, x):
        return 1 / (np.exp(-x) + 1)
    
    def predict(self, image_path):
        image = preprocess_image(image_path=image_path)
        start = time.time()
        output = self.session.run(
            [self.output_name],
            {
                self.input_name: image
            }
        )
        end = time.time()
        logits = float(output[0][0][0])
        probability = float(self.sigmoid(logits))
        
        if probability >= 0.5:
            prediction = CLASS_NAMES[1]
            confidence = probability * 100
        else:
            prediction = CLASS_NAMES[0]
            confidence = (1 - probability) * 100

        return {
            "prediction": prediction,
            "confidence": round(confidence, 2),
            "time": round(end - start, 4)
        }


predictor = DogCatPredictor()