# -*- coding: utf-8 -*-
"""
Modeling.py

@author: Soo
"""

from tensorflow.keras.models import load_model
from skimage import io
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten
from tensorflow.python.client import device_lib
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten 
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from skimage import io
import matplotlib.pyplot as plt

# 기존 모델 로딩
model_original = load_model('C:/ITWILL/AI_Interview_App/Scripts/files/emotion_model.hdf5', compile=False)

model_original.summary()










########################################
# Save Model - HDF5 형식 
########################################
model.save('keras_model_iris.h5')
print('model saved...')












































































































































































