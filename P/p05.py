# Librerias necesarias
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Abrimos la imagen
imagen = io.imread("tmp/img0.jpeg")
imagen_g = rgb2gray(imagen)

# Filtros: sobel, roberts, prewitt
filtros = [filters.sobel, filters.roberts, filters.prewitt]

for filtro in filtros:
    # Aplicamos cada uno de los filtros
    img_fil = filtro(imagen_g)
    print(str(filtro))
    #print("a:s%", filtro.name)
    #img_fil.save(filtro+'.jepg')
    # Mostramos los resultados 
    plt.imshow(img_fil)
    plt.show()