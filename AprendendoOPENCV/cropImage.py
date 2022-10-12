from ctypes import resize
import cv2
from imutils import paths
import shutil


def cropImages():
    y = 0
    x = 0
    h = 24
    w = 32
    numeroPos = 0
    numeroNeg = 0
    Nimg = 0

    imagemPath = list(paths.list_images('imagens/'))

    for z in imagemPath:
        shutil.copy(z, z.replace(
            z, 'imagensOrganizadas/' + str(Nimg) + '.png'))

        img = cv2.imread('imagensOrganizadas/' + str(Nimg) +
                         '.png', cv2.IMREAD_GRAYSCALE)
        resize_image = cv2.resize(img, (640, 480))
        cv2.imshow('img1', resize_image)
        cv2.waitKey(0)

        for i in range(20):
            for j in range(20):
                if (i == 4 and j == 4 or i==4 and j == 5 or i == 4 and j == 12 or i == 14 and j == 6 or i == 14 and j == 14 or i == 15 and j == 14):
                    croped = resize_image[y:y + h, x:x + w]
                    cv2.imwrite('pos/' + str(numeroNeg) + '.png', croped)
                    numeroNeg += 1
                    x += 32
                else:
                    croped = resize_image[y:y + h, x:x + w]
                    cv2.imwrite('neg/' + str(numeroNeg) + '.png', croped)
                    numeroNeg += 1
                    x += 32
            x = 0
            y += 24
        x = 0
        y = 0
        Nimg += 1


cropImages()
