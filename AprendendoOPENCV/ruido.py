from PIL import Image
import math


def moire(source, target, angle, distance, offsetx=2, offsety=2):

    # imagem de entrada
    img = Image.open(source)
    pm = img.load()
    # imagem de saída (usando a mesma para gerar sobreposição)
    imgout = Image.open(source)
    pmout = imgout.load()

    # valores para as transformações
    cosseno = math.cos(angle)
    seno = math.sin(angle)
    # distância em cada eixo
    dx = distance * cosseno
    dy = distance * seno

    for x in range(0, img.size[0], offsetx):
        for y in range(0, img.size[1], offsety):
            # calcula coordenada transformada (rotação + deslocamento)
            x2, y2 = dx + math.floor(x * cosseno - y * seno), dy + \
                math.floor(x * seno + y * cosseno)
            # ajusta valores fora da imagem (como se a mesma repetisse infinitamente)
            if x2 < 0:
                x2 = img.size[0] + x2
            elif x2 >= img.size[0]:
                x2 = x2 - img.size[0]
            if y2 < 0:
                y2 = img.size[1] + y2
            elif y2 >= img.size[1]:
                y2 = y2 - img.size[1]
            # desenha ponto transformado
            pmout[x, y] = pm[x2, y2]
    imgout.save(target)


moire('pos/0.jpg', 'test/test.png', math.pi / 5, 0, 5, 5)
