from flask import Flask, render_template, request, url_for, redirect, session
import os.path
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np

app = Flask(__name__)


def upload():
    img = request.files["img"]
    r, e = os.path.splitext(img.filename)
    img_path = "static/images/predict" + e
    img.save(img_path)
    return "static\\images\\predict" + e


@app.route('/', methods=['POST', 'GET'])
def detection():  # put application's code here
    if request.method == 'POST':
        path = upload()
        return "<p>"+path+"</p>"
    else:
        return render_template('detection.html')


if __name__ == '__main__':
    app.run()
