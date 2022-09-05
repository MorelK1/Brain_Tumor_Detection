from flask import Flask, render_template, request, url_for, redirect, session
# import os.path
# from keras.models import load_model
# from keras.preprocessing import image
# from PIL import Image
# import numpy as np

app = Flask(__name__)


@app.route('/')
def detection():  # put application's code here
    return render_template('detection.html')


if __name__ == '__main__':
    app.run()
