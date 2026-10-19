# Axel Guzman 0070
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Rutas dinámicas
dir_script = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(dir_script, "..", "img-original-0070", "Volkswagen.jpg")

# 2. Cargar imagen
img = cv2.imread(ruta_imagen)

if img is None:
    print("Error: No se encontró la imagen en img-original-0070/Volkswagen.jpg")
else:
    # Convertir BGR a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Extraer canales
    R, G, B = cv2.split(img_rgb)

    # Matriz de ceros del mismo tamaño que un canal
    ceros = np.zeros_like(R)

    # Crear imágenes donde solo resalta UN color
    canal_rojo = cv2.merge((R, ceros, ceros))     # Solo Rojo
    canal_verde = cv2.merge((ceros, G, ceros))    # Solo Verde
    canal_azul = cv2.merge((ceros, ceros, B))     # Solo Azul

    # Visualización con Matplotlib
    fig = plt.figure(figsize=(10, 8))

    # CANAL ROJO (Se ve en ROJO)
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(canal_rojo)
    ax1.set_title("CANAL ROJO")
    ax1.axis("off")

    # CANAL VERDE (Se ve en VERDE)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(canal_verde)
    ax2.set_title("CANAL VERDE")
    ax2.axis("off")

    # CANAL AZUL (Se ve en AZUL)
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.imshow(canal_azul)
    ax3.set_title("CANAL AZUL")
    ax3.axis("off")

    # RECONSTRUCCIÓN / ORIGINAL
    imgre = cv2.merge((R, G, B))
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.imshow(imgre)
    ax4.set_title("VOLKSWAGEN ORIGINAL")
    ax4.axis("off")

    plt.tight_layout()
    plt.show()

    print("Practica terminada correctamente")

print("programa realizado por Axel Guzman 0070")