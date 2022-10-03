from ctypes import resize
import cv2
from imutils import paths
import shutil


def cropImages():
    y = 0
    x = 0
    h = 48
    w = 64
    numero = 0
    Nimg = 0

    imagemPath = list(paths.list_images('imagens/'))

    for z in imagemPath:
        shutil.copy(z, z.replace(z, 'imagensOrganizadas/' + str(Nimg) + '.png'))

        img = cv2.imread('imagensOrganizadas/' + str(Nimg) + '.png', cv2.IMREAD_GRAYSCALE)
        resize_image = cv2.resize(img, (640, 480))

        for i in range(10):
            for j in range(10):
                if (i == 2 and j == 2) or (i == 2 and j == 6) or (i == 7 and j == 3) or (i == 7 and j == 7):
                    croped = resize_image[y:y + h, x:x + w]
                    cv2.imwrite('pos/' + str(numero) + '.png', croped)
                    numero += 1
                    x += 64
                else:
                    croped = img[y:y + h, x:x + w]
                    cv2.imwrite('neg/' + str(numero) + '.png', croped)
                    numero += 1
                    x += 64
            x = 0
            y += 48
        x = 0
        y = 0
        Nimg += 1



cropImages()