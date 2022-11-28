from PIL import Image
import numpy
im = Image.open("Girabandeira\\Capturar.PNG")
#im = im.resize((400,400))
im_matriz = numpy.asarray(im)
for linha in range(im_matriz.shape[0]):
    for coluna in range(im_matriz.shape[1]):
        im_matriz[linha][coluna][2]=0
        for banda in range(0,4): #RGBA
            if banda == 0 or banda == 2 and im_matriz[linha][coluna][banda] <= 255:
                im_matriz[linha][coluna][banda] += coluna/im_matriz.shape[1]*255
            #if banda == 1:
            #    im_matriz[linha][coluna][banda] -= coluna/im_matriz.shape[1]*255
            else:
                pass
                #im_matriz[linha][coluna][banda] = 0
            #if banda == 1 and pixel[banda] >=0:
            #    pixel[banda] +=-1
im_nova = Image.fromarray(im_matriz,'RGBA')
im_nova.show()