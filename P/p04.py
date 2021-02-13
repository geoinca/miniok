import random
from PIL import Image

def salpimienta(imagen,porcentaje):
    tamano=imagen.size[0]*imagen.size[1]
    auxiliar=(tamano*porcentaje)

    if imagen.mode=='RGB':
        datoMinimo=(0,0,0)
        datoMaximo=(255,255,255)
    elif imagen.mode=='L':
        datoMinimo=0
        datoMaximo=255
    
    for x in range(auxiliar):
        coordenada_x=random.randrange(2,imagen.width-2)
        coordenada_y=random.randrange(2,imagen.height-2)

        imagen.putpixel((coordenada_x,coordenada_y),datoMaximo)
        imagen.putpixel((coordenada_x+1,coordenada_y),datoMaximo)
        imagen.putpixel((coordenada_x,coordenada_y+1),datoMaximo)
        imagen.putpixel((coordenada_x+1,coordenada_y+1),datoMaximo)

    for x in range(auxiliar):
        coordenada_x=random.randrange(2,imagen.width-2)
        coordenada_y=random.randrange(2,imagen.height-2)

        imagen.putpixel((coordenada_x,coordenada_y),datoMinimo)
        imagen.putpixel((coordenada_x+1,coordenada_y),datoMinimo)
        imagen.putpixel((coordenada_x,coordenada_y+1),datoMinimo)
        imagen.putpixel((coordenada_x+1,coordenada_y+1),datoMinimo) 

    imagen.save('solvsp.jpeg')
    return None
  

foto = Image.open('tmp/img4.jpeg')
salpimienta(foto,1)