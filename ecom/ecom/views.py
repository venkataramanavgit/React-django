# from __future__ import division, print_function
# # coding=utf-8
# import sys
# import os
# import glob
# import re
# import numpy as np
# import json

# # Keras
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
# from keras.applications.mobilenet import preprocess_input

# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

# # Flask utils
# from flask import Flask, redirect, url_for, request, render_template
# from werkzeug.utils import secure_filename
# #from gevent.pywsgi import WSGIServer

# with open("mapping.json") as f:
#     mapped_classes = json.load(f)
#     f.close()



# # Model saved with Keras model.save()
# MODEL_PATH ='mobilenet_model.h5'

# # Load your trained model
# model = load_model(MODEL_PATH)


# def model_predict(img_path, model):
#     img = image.load_img(img_path, target_size=(224, 224))

#     # Preprocessing the image
#     x = image.img_to_array(img)
#     ## Scaling
#     x=x/255
#     x = np.expand_dims(x, axis=0)

#     preds = model.predict(x)
#     preds=np.argmax(preds, axis=1)
#     preds = mapped_classes.get(str(preds[0]))

#     return preds


# @app.route('/', methods=['GET'])
# def index():
#     # Main page
#     return render_template('index.html')

from django.shortcuts import render

def index(request):
    return render(request, 'pd/index.html')
# def upload():
#     if request.method == 'POST':
#         # Get the file from post request
#         f = request.files['file']

#         # Save the file to ./uploads
#         basepath = os.path.dirname(__file__)
#         file_path = os.path.join(
#             basepath, 'uploads', secure_filename(f.filename))
#         f.save(file_path)

#         # Make prediction
#         preds = model_predict(file_path, model)
#         result=preds
#         os.remove(file_path)
#         return result
#     return None

