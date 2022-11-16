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

data_dir = tf.keras.utils.get_file(
    "tests.zip",
    "https://github.com/TheCondorr/TIPE_road_sign_detection/blob/main/Tests.zip?raw=true",
    extract=False)

with zipfile.ZipFile(data_dir, 'r') as zip_ref:
    zip_ref.extractall('/content/datasets')
