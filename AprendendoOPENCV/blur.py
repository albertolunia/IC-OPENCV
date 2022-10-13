from ctypes import resize
import cv2
from imutils import paths
import shutil
import numpy as np

def blur():

    Nimg = 0
    
    imagemPath = list(paths.list_images('pos/'))

    Nrot = len(imagemPath)

    for z in imagemPath:

        img = cv2.imread('pos/' + str(Nimg) + '.png')
        filter_blur=cv2.blur(img,ksize=(2,2))
        cv2.imwrite('pos/'+ str(Nrot) + '.png', filter_blur)
        Nimg += 1
        Nrot += 1

blur()