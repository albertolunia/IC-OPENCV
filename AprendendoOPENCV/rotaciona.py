from ctypes import resize
import cv2
from imutils import paths
import shutil


def rotaciona():
    Nimg = 0
    
    imagemPath = list(paths.list_images('pos/'))

    Nrot = len(imagemPath)

    for z in imagemPath:
        img = cv2.imread('pos/' + str(Nimg) + '.png')
        (rows, cols) = img.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
        res = cv2.warpAffine(img, M, (cols, rows))

        cv2.imwrite('pos/'+ str(Nrot) + '.png', res)
        Nimg += 1
        Nrot += 1

rotaciona()

