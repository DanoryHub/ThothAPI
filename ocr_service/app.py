import os
import glob

import pytesseract
from PIL import Image
from flask import Flask, request
from sqlalchemy.orm import sessionmaker

from db_connect import data_insert, engine, checkout_orm

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/health-check", methods=["GET"])
def check():
    return {"status": "OK"}

@app.route("/ocr", methods=["POST"])
def recognize():
    result = {}
    files = glob.glob("/app/images/*")
    for image in files:
        name = image.split("/")[3].split(".")[0]
        img = Image.open(image)
        text = pytesseract.image_to_string(img, lang="rus+eng")
        result[name] = text
        os.remove(image)

    data_insert(**result)
    
    return result

app.run(host="0.0.0.0")