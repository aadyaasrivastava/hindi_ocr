import easyocr
from numpy import asarray
import numpy
import cv2
from PIL import Image
from PIL import ImageFilter

def get_text(image):
    
    imagecv = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    
    

    pil_image = image.filter(ImageFilter.EDGE_ENHANCE)
    #pil_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    data = asarray(pil_image)
    reader = easyocr.Reader(['hi'])
    result = reader.readtext(data, batch_size=8)

    text = []
    coo = []

    for i in result:

        cord = i[0]

        x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
        x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

    

        text.append(i[1:])

        coo.append([(x_min, y_min), (x_max, y_max)])

		
    return(text,coo,pil_image)
