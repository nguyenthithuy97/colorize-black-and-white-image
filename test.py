import os
import base64
from io import BytesIO

from keras.preprocessing import image
from flask import Flask, make_response, request, render_template
from werkzeug.exceptions import BadRequest
from serving import (
    load_model,
    evaluate_input,
    evaluate_input_mat
)
from support import (
	show_img,
	read_img
)

CWD_PATH = os.getcwd()

load_model()
def colorsize(image_name):
	PATH_TO_IMAGE = os.path.join(CWD_PATH, "images", image_name)
	img = evaluate_input(PATH_TO_IMAGE)
	# img = evaluate_input_mat(PATH_TO_IMAGE)

	show_img(image.img_to_array(img))

while (True):  
	# image_name format is .jpg .png
    inp = input('image_name = ')
    if inp == '':
        break
    colorsize(inp)