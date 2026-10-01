import numpy as np
import cv2
# Vision artificial Act10 NC 0106
# Lee la imagen en escala de grises
img = cv2.imread("tierra.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("tierra 0106", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Linea
print("La linea 0106")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("tierra 0106", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#circulo
print("El circulo 0106")

# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

cv2.imshow("tierra 0106", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Texto
print("texto 0106")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Hola soy yo 0106", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

cv2.imshow("tierra 0106", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("")