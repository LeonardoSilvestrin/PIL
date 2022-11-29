from PIL import Image
im1 = Image.open('Simples\\Bandeira.PNG').resize((500,350))
x,y = im1.size
caixa = (0,0,x/2,y/2)
croped = im1.crop(caixa)
croped.paste(im1,(0,0,int(x/2),int(y/2)))
im1.show()