from ctypes import resize
import cv2
from imutils import paths
import numpy as np


def test():

    FILE_NAME = 'pos/10.png'
    M = np.float32([[1, 0, 20], [0, 1, 20]])

    img = cv2.imread(FILE_NAME)
    (rows, cols) = img.shape[:2]

    res = cv2.warpAffine(img, M, (cols, rows))

    cv2.imwrite('result10.jpg', res)


test()
