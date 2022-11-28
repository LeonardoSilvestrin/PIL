from PIL import Image

im = Image.open('Simples\\Capturar.PNG')
im = im.convert('RGB')
im2 = Image.eval(im,(lambda pix: 254-pix))
im.show()
im2.show()