# -*- coding: utf-8 -*-
"""
Modeling.py

1. Transfer Learning
 - 
2. Fine Tuning


"""

from tensorflow.keras.models import load_model
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Dropout, Flatten 
from tensorflow.keras.optimizers import RMSprop




# 기존 모델 로딩
model_original = load_model('C:/ITWILL/AI_Interview_App/Scripts/files/emotion_model.hdf5', compile=False)

model_original.summary()


# Model 생성
model = Sequential()

input_shape = (48, 48, 1)

model.add(Conv2D(50, kernelsize))










########################################
# Save Model - HDF5 형식 
########################################
model.save('keras_model_iris.h5')
print('model saved...')












































































































































































