from flask import Flask, render_template, request
from PIL import Image
from easy_ocr import get_text
import base64
import cv2
import numpy

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html", result = False)

@app.route('/get_text_from_ocr', methods=['POST'])
def get_text_from_ocr():

    image = request.files["image"]

    image_mod = Image.open(image)

    result_text,coo = get_text(image_mod)

    text_final = ""
    percent_result = []

    for rt in result_text:
        text_final += rt[0] + " "
        percent_result.append(float(rt[1]))

    per_avg = sum(percent_result)/len(percent_result)

    result_text = [(text_final, per_avg)]

    imagecv = cv2.cvtColor(numpy.array(image_mod), cv2.COLOR_RGB2BGR)
    for c in coo:
        cv2.rectangle(imagecv,c[0], c[1],(255,0,0),1)

    _, im_arr = cv2.imencode('.jpg', imagecv)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)

    return render_template("index.html", result = True, text = result_text, image64 = im_b64.decode("utf-8") )
    
app.run(debug=True)
