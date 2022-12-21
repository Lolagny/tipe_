from re import S
import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import datetime
from tensorflow import keras
import tensorflow as tf
import pathlib
import os
import zipfile

pieton_train = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "pieton.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/pieton.zip?raw=true",
    extract=False)

pieton_val = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "pieton_val.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/pieton_val.zip?raw=true",
    extract=False)

stop_train = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "stop.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/stop.zip?raw=true",
    extract=False)                            

stop_val = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "stop_val.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/stop_val.zip?raw=true",
    extract=False)

vitesse_train = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "vitesse.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/vitesse.zip?raw=true",
    extract=False)

vitesse_val = tf.keras.utils.get_file(                                     #Récupération du dossier d'images de Github par Keras
    "vitesse_val.zip",
    "https://github.com/Lolagny/tipe_/blob/new_database/vitesse_val.zip?raw=true",
    extract=False)


with zipfile.ZipFile(pieton_train, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/datasets')

with zipfile.ZipFile(pieton_val, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/dataval')

with zipfile.ZipFile(stop_train, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/datasets')

with zipfile.ZipFile(stop_val, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/dataval')

with zipfile.ZipFile(vitesse_train, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/datasets')

with zipfile.ZipFile(vitesse_val, 'r') as zip_ref:       #Extraction du zip
    zip_ref.extractall('/content/dataval')


data_dir = pathlib.Path('/content/datasets')     #Chemin du dossier contenant les images
print(data_dir)
print(os.path.abspath(data_dir))

data_val = pathlib.Path('/content/dataval')
print(data_val)
print(os.path.abspath(data_val))

image_count = len(list(data_dir.glob('*/*')))     #Vérification du nombre d'images
print(image_count)
image_count = len(list(data_val.glob('*/*')))     #Vérification du nombre d'images
print(image_count)

batch_size = 20        #Envoi des images 3 par 3
img_height = 200      #Initialisation des images de taile carrée
img_width = 200

train_data = tf.keras.preprocessing.image_dataset_from_directory(   #Fonction de pre-process par Keras
  data_dir,
  validation_split=0.2,
  subset="training",                             #Jeu de données de training
  seed=42,
  image_size=(img_height, img_width),
  batch_size=batch_size,
  )

val_data = tf.keras.preprocessing.image_dataset_from_directory(     #Fonction de pre-process par Keras
  data_val,
  validation_split=0.2,
  subset="validation",                          #Jeu de données de validation
  seed=42,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_data.class_names          #Définition des classes
print(class_names)

from tensorflow.keras import layers

num_classes = 3

model = tf.keras.Sequential([                                   #Procédé du réseau de neurones
    layers.experimental.preprocessing.Rescaling(1./255),
    layers.Conv2D(128,4, activation='relu'),                    #Alternance convolution / pooling
    layers.MaxPooling2D(),
    layers.Conv2D(64,4, activation='relu'),                     #Le but des couches de convolution est de détecter
    layers.MaxPooling2D(),                                      #les éléments qui permettent de reconnaitre
    layers.Conv2D(32,4, activation='relu'),                     #l'image
    layers.MaxPooling2D(),
    layers.Conv2D(16,4, activation='relu'),                     #Les couches de pooling permettent de réduire de 
    layers.MaxPooling2D(),                                      #au maximum les images
    layers.Flatten(), 
    layers.Dense(64,activation='relu'),                         #On utilise la fonction d'activation relu
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'],)

logdir="logs"

tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir,histogram_freq=1, write_images=logdir,
                                                   embeddings_data=train_data)

model.fit( 
    train_data,
  validation_data=val_data,
  epochs=5,
  callbacks=[tensorboard_callback]
)

model.summary()

from google.colab import files
file_to_predict = files.upload()
for file_ in file_to_predict:
    image_to_predict = cv2.imread(file_,cv2.IMREAD_COLOR)
    plt.imshow(cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2RGB))
    plt.show()
    img_to_predict = np.expand_dims(cv2.resize(image_to_predict,(200,200)), axis=0) 
    res = model.predict(img_to_predict)
    print(res)
    res = class_names[np.argmax(res)]
    print(res)