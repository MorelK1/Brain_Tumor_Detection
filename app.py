from flask import Flask, render_template, request, url_for, redirect, session
import os.path
import numpy
import tensorflow
from keras.models import load_model
from PIL import Image
import cv2

app = Flask(__name__)


@app.route('/')
def detection():  # put application's code here
    return render_template('detection.html')


if __name__ == '__main__':
    app.run()
