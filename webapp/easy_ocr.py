import easyocr
from numpy import asarray
import numpy
import cv2

def get_text(image):
    
    imagecv = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)

    data = asarray(image)
    reader = easyocr.Reader(['hi'])
    result = reader.readtext(data)

    text = []
    coo = []

    for i in result:

        cord = i[0]

        x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
        x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

        # result = ((coo,text,per),(coo,text,per),(coo,text,per),.........)

        # i = (coo,text,per)

        # text = (text,per)

        text.append(i[1:])

        coo.append([(x_min, y_min), (x_max, y_max)])


    return(text,coo
