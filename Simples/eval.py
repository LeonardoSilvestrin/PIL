from PIL import Image

im = Image.open('Simples\\Bandeira.PNG')
im = im.convert('RGB')

im2 = Image.eval(im,(lambda pix: 254-pix))

im.show("BANDEIRA ORIGINAL")
im2.show("BANDEIRA INVERTIDA")