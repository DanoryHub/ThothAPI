from PIL import Image
from flask import Flask, request

from preprocess import crop_image_template

app = Flask(__name__)

@app.route("/health-check", methods=["GET"])
def check():
    return {"status": "OK"}

@app.route("/preprocess", methods=["POST"])
def preprocess():
    image = request.files["image"]
    image = Image.open(image)

    document_type = request.form["DocumentType"]

    croped_images = crop_image_template(image, document_type)

    for key, image in croped_images.items():
        image.save("images/" + key + ".png")

    return {"status": "OK"}



app.run(host="0.0.0.0", port=5001)