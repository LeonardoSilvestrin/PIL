from PIL import Image
import numpy

def rodacirculo(imagem, x, y, raio, angulo):
    box = (x-raio, y-raio, x+raio+1, y+raio+1)
    crop = imagem.crop(box=box)
    crop_arr = numpy.asarray(crop)
    # build the cirle mask
    mask = numpy.zeros((2*raio+1, 2*raio+1))
    for i in range(crop_arr.shape[0]):
        for j in range(crop_arr.shape[1]):
            if (i-raio)**2 + (j-raio)**2 <= raio**2:
                mask[i,j] = 1
    # create the new circular image
    sub_img_arr = numpy.empty(crop_arr.shape ,dtype='uint8')
    sub_img_arr[:,:,:3] = crop_arr[:,:,:3]
    sub_img_arr[:,:,3] = mask*255
    sub_img = Image.fromarray(sub_img_arr, "RGBA").rotate(angulo)
    i2 = imagem.copy()
    i2.paste(sub_img, box[:2], sub_img.convert('RGBA'))
    return i2

if __name__ == '__main__':
    im = Image.open("Girabandeira\\Capturar.PNG")
    #im = im.resize((500,350))
    x = int(im.size[0]/2)
    y = int(im.size[1]/2)
    im2 = rodacirculo(im,x,y,220,90)
    im.show()
    im2.show()