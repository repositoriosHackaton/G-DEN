import tensorflow as tf  # Importa TensorFlow para construir y entrenar modelos de machine learning
import json  # Importa la biblioteca JSON para trabajar con archivos JSON
import numpy as np  # Importa NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa Matplotlib para la visualización de datos
import os  # Importa os para trabajar con el sistema de archivos

# Abre el archivo JSON y carga los datos
with open('data.json', 'r') as f:  # Abre el archivo 'data.json' en modo lectura
    data = json.load(f)  # Carga los datos del archivo JSON en la variable 'data'

# Extrae los datos de entrenamiento y pruebas
datos_entrenamiento = data['train']  # Extrae la parte de datos de entrenamiento
datos_pruebas = data['test']  # Extrae la parte de datos de prueba

# Extrae los metadatos
metadatos = data['dataset_info']  # Extrae la información del conjunto de datos

# Define las clases (se asume que las etiquetas están en los metadatos)
nombres_clases = ['neurotipico', 'autismo']  # Lista de nombres de las clases

# Función para cargar y normalizar las imágenes
def cargar_y_normalizar(ruta, etiqueta):
    img = tf.io.read_file(ruta)  # Lee el archivo de imagen desde la ruta especificada
    img = tf.image.decode_png(img, channels=1)  # Decodifica la imagen PNG en un tensor, manteniendo solo 1 canal (grayscale)
    img = tf.image.convert_image_dtype(img, tf.float32)  # Convierte la imagen a tipo de dato float32
    img = tf.image.resize(img, [128, 128])  # Redimensiona la imagen a 128x128 píxeles
    img /= 255.0  # Normaliza los valores de los píxeles a un rango de [0, 1]
    return img, etiqueta  # Devuelve la imagen procesada y su etiqueta

# Construye las rutas completas a los archivos de imagen
def construir_ruta_completa(imagen_path):
    return os.path.join(metadatos['data_dir'], imagen_path)  # Combina la ruta base y el path relativo de la imagen

# Cargar los datos de entrenamiento
rutas_entrenamiento = [construir_ruta_completa(item['image_path']) for item in datos_entrenamiento]  # Lista de rutas completas para las imágenes de entrenamiento
etiquetas_entrenamiento = [item['label'] for item in datos_entrenamiento]  # Lista de etiquetas para las imágenes de entrenamiento

# Cargar los datos de prueba
rutas_pruebas = [construir_ruta_completa(item['image_path']) for item in datos_pruebas]  # Lista de rutas completas para las imágenes de prueba
etiquetas_pruebas = [item['label'] for item in datos_pruebas]  # Lista de etiquetas para las imágenes de prueba

# Crear los datasets de TensorFlow
datos_entrenamiento = tf.data.Dataset.from_tensor_slices((rutas_entrenamiento, etiquetas_entrenamiento))  # Crea un dataset de TensorFlow a partir de las rutas y etiquetas de entrenamiento
datos_pruebas = tf.data.Dataset.from_tensor_slices((rutas_pruebas, etiquetas_pruebas))  # Crea un dataset de TensorFlow a partir de las rutas y etiquetas de prueba

# Mapea la función de carga y normalización a los datasets
datos_entrenamiento = datos_entrenamiento.map(cargar_y_normalizar)  # Aplica la función de carga y normalización a cada elemento del dataset de entrenamiento
datos_pruebas = datos_pruebas.map(cargar_y_normalizar)  # Aplica la función de carga y normalización a cada elemento del dataset de prueba

# Cachea los datasets para mejorar el rendimiento
datos_pruebas = datos_pruebas.cache()  # Cachea el dataset de prueba en memoria
datos_entrenamiento = datos_entrenamiento.cache()  # Cachea el dataset de entrenamiento en memoria

# Construye y compila el modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(128, 128, 1)),  # Capa que aplana la entrada de 128x128x1 a un vector de 16384 elementos
    tf.keras.layers.Dense(50, activation=tf.nn.relu),  # Capa densa totalmente conectada con 50 neuronas y función de activación ReLU
    tf.keras.layers.Dense(50, activation=tf.nn.relu),  # Otra capa densa con 50 neuronas y activación ReLU
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)  # Capa de salida con 2 neuronas y activación softmax para clasificación
])

modelo.compile(
    optimizer='adam',  # Optimizador Adam
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),  # Función de pérdida de entropía cruzada para etiquetas enteras
    metrics=['accuracy']  # Métrica de evaluación: exactitud
)

# Obtén el número de ejemplos de entrenamiento y pruebas
num_ej_entrenamiento = metadatos['splits']['train']['num_examples']  # Número de ejemplos en el conjunto de entrenamiento
num_ej_pruebas = metadatos['splits']['test']['num_examples']  # Número de ejemplos en el conjunto de prueba

# Define el tamaño del lote
TAMANO_LOTE = 1  # Tamaño de lote para entrenamiento y pruebas

# Prepara los datasets para entrenamiento
datos_entrenamiento = datos_entrenamiento.repeat().shuffle(num_ej_entrenamiento).batch(TAMANO_LOTE)  # Repite, baraja y agrupa el dataset de entrenamiento
datos_pruebas = datos_pruebas.batch(TAMANO_LOTE)  # Agrupa el dataset de prueba en lotes

import math  # Importa la biblioteca math para operaciones matemáticas

# Entrena el modelo
historial = modelo.fit(datos_entrenamiento, epochs=5, steps_per_epoch=math.ceil(num_ej_entrenamiento / TAMANO_LOTE))  # Entrena el modelo por 5 épocas

# Predice con los datos de prueba y grafica los resultados
for imagenes_prueba, etiqueta_prueba in datos_pruebas.take(1):  # Toma un lote de datos de prueba
    imagenes_prueba = imagenes_prueba.numpy()  # Convierte las imágenes de prueba a numpy array
    etiqueta_prueba = etiqueta_prueba.numpy()  # Convierte las etiquetas de prueba a numpy array
    predicciones = modelo.predict(imagenes_prueba)  # Genera predicciones con el modelo

# Función para graficar una imagen y su predicción
def graficar_imagen(i, arr_predicciones, etiquetas_reales, imagenes):
    if i < len(arr_predicciones):  # Verifica que el índice esté dentro del rango de predicciones
        arr_predicciones, etiqueta_real, img = arr_predicciones[i], etiquetas_reales[i], imagenes[i]  # Extrae la predicción, etiqueta real e imagen
        plt.grid(False)  # Elimina la cuadrícula del gráfico
        plt.xticks([])  # Elimina las marcas en el eje x
        plt.yticks([])  # Elimina las marcas en el eje y

        plt.imshow(img[..., 0], cmap=plt.cm.binary)  # Muestra la imagen en escala de grises

        etiqueta_prediccion = np.argmax(arr_predicciones)  # Obtiene la clase predicha
        color = 'green' if etiqueta_prediccion == etiqueta_real else 'red'  # Determina el color del texto según si la predicción es correcta

        plt.xlabel('{} {:2.0f}% ({})'.format(
            nombres_clases[etiqueta_prediccion],  # Nombre de la clase predicha
            100 * np.max(arr_predicciones),  # Porcentaje de certeza de la predicción
            nombres_clases[etiqueta_real]  # Nombre de la clase real
        ), color=color)  # Etiqueta el gráfico con la predicción, certeza y clase real

# Función para graficar valores de predicciones en un arreglo de barras
def graficar_valor_arreglo(i, arr_predicciones, etiqueta_real):
    arr_predicciones, etiqueta_real = arr_predicciones[i], etiqueta_real[i]  # Extrae la predicción y etiqueta real
    plt.grid(False)  # Elimina la cuadrícula del gráfico
    plt.xticks([])  # Elimina las marcas en el eje x
    plt.yticks([])  # Elimina las marcas en el eje y
    grafica = plt.bar(range(len(nombres_clases)), arr_predicciones, color='#777777')  # Crea un gráfico de barras con las predicciones
    plt.ylim([0, 1])  # Define el límite del eje y de 0 a 1
    etiqueta_prediccion = np.argmax(arr_predicciones)  # Obtiene la clase predicha

    grafica[etiqueta_prediccion].set_color('red')  # Colorea en rojo la barra de la clase predicha
    grafica[etiqueta_real].set_color('green')  # Colorea en verde la barra de la clase real

# Código para graficar imágenes y barras de predicciones
filas = 1  # Define el número de filas de gráficos
columnas = 1  # Define el número de columnas de gráficos
num_imagenes = filas * columnas  # Calcula el número total de imágenes a mostrar
plt.figure(figsize=(2 * 2 * columnas, 2 * filas))  # Crea una figura de tamaño adecuado para mostrar los gráficos
for i in range(min(num_imagenes, len(predicciones))):  # Recorre las predicciones hasta el máximo entre num_imagenes y la longitud de predicciones
    plt.subplot(filas, 2 * columnas, 2 * i + 1)  # Añade un subgráfico para la imagen
    graficar_imagen(i, predicciones, etiqueta_prueba, imagenes_prueba)  # Llama a la función para graficar la imagen
    plt.subplot(filas, 2 * columnas, 2 * i + 2)  # Añade un subgráfico para el gráfico de barras
    graficar_valor_arreglo(i, predicciones, etiqueta_prueba)  # Llama a la función para graficar el gráfico de barras

plt.tight_layout()  # Ajusta el diseño para evitar solapamientos

# Solicitar al usuario ingresar el nombre del paciente
nombre_paciente = input("Ingrese el nombre del paciente: ")  # Pide al usuario que ingrese el nombre del paciente

# Crea una carpeta para guardar los gráficos si no existe
carpeta_resultados = 'resultados'  # Define el nombre de la carpeta de resultados
if not os.path.exists(carpeta_resultados):  # Comprueba si la carpeta no existe
    os.makedirs(carpeta_resultados)  # Crea la carpeta de resultados

# Guarda el gráfico en la carpeta de resultados con el nombre del paciente
nombre_archivo = f'{nombre_paciente}_grafico_resultados.png'  # Define el nombre del archivo con el nombre del paciente
ruta_grafico = os.path.join(carpeta_resultados, nombre_archivo)  # Crea la ruta completa del archivo
plt.savefig(ruta_grafico)  # Guarda el gráfico en la ruta especificada

# Muestra el gráfico en la consola o en una ventana
plt.show()  # Muestra el gráfico
