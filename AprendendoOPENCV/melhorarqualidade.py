from ctypes import resize
import cv2
from imutils import paths
import shutil
import numpy as np


def melhora():

    Nimg = 0

    imagemPath = list(paths.list_images('pos/'))

    Nrot = len(imagemPath)

    for z in imagemPath:

        img = cv2.imread('pos/' + str(Nimg) + '.png')
        kernel = np.array([[0, -1,  0],
                           [-1,  5, -1],
                           [0, -1,  0]])
        filter2d = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
        cv2.imwrite('pos/'+ str(Nrot) + '.png', filter2d)
        Nimg += 1
        Nrot += 1

melhora()
