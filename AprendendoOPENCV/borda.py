from ctypes import resize
import cv2
from imutils import paths
import shutil

def borda():
    Nimg = 0
    
    imagemPath = list(paths.list_images('pos/'))

    for z in imagemPath:
        img = cv2.imread('pos/' + str(Nimg) + '.png') 
        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite('test/' + str(Nimg) + '.png', edges)
        Nimg += 1

borda()