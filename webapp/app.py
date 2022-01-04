from flask import Flask, render_template, request, Response, session, send_file
from PIL import Image
from easy_ocr import get_text
import base64
import cv2
import numpy
from convert import *

from gtts import gTTS

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html", result = False)

@app.route('/get_text_from_ocr', methods=['POST',"GET"])
def get_text_from_ocr():

    image = request.files["image"]

    image_mod = Image.open(image)

    result_text,coo,pil_image = get_text(image_mod)

    text_final = ""
    percent_result = []

    for rt in result_text:
        text_final += rt[0] + " "
        percent_result.append(float(rt[1]))

    converter_1(text_final)
    converter(text_final)

    myobj = gTTS(text=text_final, lang="hi", slow=False)

    myobj.save("static/audio/hindi_audio.mp3")

    # session["result"] = text_final

    per_avg = sum(percent_result)/len(percent_result)

    result_text = [(text_final, per_avg)]

    imagecv = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    for c in coo:
        cv2.rectangle(imagecv,c[0], c[1],(255,0,0),1)

    _, im_arr = cv2.imencode('.jpg', imagecv)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)

    return render_template("index.html", result = True, text = result_text, image64 = im_b64.decode("utf-8") )
    
@app.route("/get-file")
def get_file():
    results = "hi i am ape"
    generator = (cell for row in results
                    for cell in row)

    return Response(generator,
                       mimetype="text/plain",
                       headers={"Content-Disposition":
                                    "attachment;filename=test.txt"})

@app.route('/downloader/pdf', methods=['POST',"GET"])
def downloader_pdf():
    # txt = session.get("result")
    # converter_1(txt)
    # print(session)
    
    # return(txt)
    return send_file("static/Download/pdf/hindi_pdf.pdf", as_attachment=True)

@app.route('/downloader/doc', methods=['POST',"GET"])
def downloader_doc():
    # txt = session["result"]
    # converter(txt)
    # return(txt)

    return send_file("static/Download/document/hindi_doc.docx", as_attachment=True)

app.run(debug=True)
