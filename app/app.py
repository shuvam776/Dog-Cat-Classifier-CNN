import os
import uuid

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER
from config import ALLOWED_EXTENSIONS

from inference import predictor


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER,exist_ok=True)


def allowed_file(filename):

    return "." in filename and \
           filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():

    if "image" not in request.files:
        return redirect("/")

    file = request.files["image"]

    if file.filename == "":
        return redirect("/")

    if not allowed_file(file.filename):
        return redirect("/")


    original_filename = secure_filename(file.filename)

    extension = original_filename.rsplit(".", 1)[1].lower()

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(
    app.config["UPLOAD_FOLDER"],
    filename
    )

    file.save(filepath)

    result = predictor.predict(filepath)

    image_url = url_for(
        "static",
        filename=f"uploads/{filename}"
    )

    return render_template(
        "index.html",
        image=image_url,
        prediction=result["prediction"],
        confidence=result["confidence"],
        inference_time=result["time"]
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )