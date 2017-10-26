# -*- coding: utf-8 -*-
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

def create_model():
    model = Sequential([
        Dense(2000, input_shape=(384,)),
        Activation('relu'),
        Dense(2000),
        Activation('relu'),
        Dense(2000),
        Activation('relu'),
        Dense(4096),
        Activation('softmax')])
    compile_model(model)
    return model

def compile_model(model):
    model.compile(optimizer='adadelta',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

def load_model(filename):
    if filename.endswith('.json'):
        json_filename = filename
        h5_filename = filename[:-5] + '.h5'
    else: # assume local filename root only
        json_filename = 'model/' + filename + '.json'
        h5_filename = 'model/' + filename + '.h5'
    json_filename.replace('\\', '/');
    h5_filename.replace('\\', '/');
    with open(json_filename, 'r') as json_file:
        model_json = json_file.read()
        json_file.close()
    model = keras.models.model_from_json(model_json)
    model.load_weights(h5_filename)
    compile_model(model)
    return model

def save_model(model, filename):
    filename = 'model/' + filename
    model.save_weights(filename + '.h5')
    model_json = model.to_json()
    with open(filename + '.json', 'w') as json_file:
        json_file.write(model_json)
