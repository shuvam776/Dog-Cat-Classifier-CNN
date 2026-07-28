# 🐶🐱 Dog vs Cat Classifier

A Flask web application that classifies Cats and Dogs using a **ResNet50 Transfer Learning model exported to ONNX**.

---

## Features

- Flask Backend
- Tailwind CSS Frontend
- ONNX Runtime Inference
- Upload Images
- Confidence Score
- Inference Time
- Docker Support
- Gunicorn Production Server

---

## Project Structure

```
dog-cat-classifier/

│
├── app.py
├── config.py
├── inference.py
├── preprocess.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── models/
│   └── resnet50.onnx
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/dog-cat-classifier.git
```

Go inside

```bash
cd dog-cat-classifier
```

Create Virtual Environment

Linux / Mac

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

## Docker

Build

```bash
docker build -t dog-cat-classifier .
```

Run

```bash
docker run -p 5000:5000 dog-cat-classifier
```

or

```bash
docker compose up --build
```

---

## Model

Place your ONNX model here

```
models/
    resnet50.onnx
```

---

## Input

RGB Image

Supported

- jpg
- jpeg
- png

Image Size

```
224 x 224
```

---

## Output

Prediction

```
Dog
```

or

```
Cat
```

Confidence

```
99.81%
```

Inference Time

```
0.012 s
```

---

## Technologies

- Python
- Flask
- ONNX Runtime
- Tailwind CSS
- Docker
- Gunicorn

---

## License

MIT