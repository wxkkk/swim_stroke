import tensorflow as tf
import keras
from keras import Model, Input, Sequential
from keras.layers import Reshape, Conv1D, Activation, MaxPool1D, Flatten, Dropout, Dense, Convolution1D, GlobalAveragePooling1D
from keras.utils import np_utils
import pandas as pd
import numpy as np

cate_list = ['Acer', 'Pterocarya', 'Quercus', 'Tilia', 'Magnolia', 'Salix', 'Zelkova', 'Betula',
             'Fagus', 'Phildelphus', 'Populus', 'Alnus', 'Arundinaria', 'Liriodendron', 'Cytisus',
              'Rhododendron', 'Eucalyptus', 'Cercis', 'Cotinus', 'Celtis', 'Cornus', 'Callicarpa',
             'Prunus', 'Ilex', 'Ginkgo', 'Liquidambar', 'Lithocarpus', 'Viburnum', 'Crataegus',
             'Morus', 'Olea', 'Castanea', 'Ulmus', 'Sorbus']

train_path = r'../../data/test_data/processed/train_file.csv'

train_file = pd.read_csv(train_path)
print(train_file.head())
# print(train_file.columns.values[0:193])

train_data = train_file[train_file.columns.values[2:]][:600]
test_data = train_file[train_file.columns.values[2:]][600:]

train_label = train_file[train_file.columns.values[1]][:600].tolist()
test_label = train_file[train_file.columns.values[1]][600:].tolist()

# train_file = pd.get_dummies(data=train_file, prefix='species')

print("train data:\n", train_data.describe(), "\ntest data:\n", test_data.describe())
print("train label:\n", train_label, "\ntest label:\n", test_label)
# print(train_label.head())

# train_data_df = pd.DataFrame(train_data)

model = Sequential()
# C1
model.add(Conv1D(filters=6, kernel_size=3, activation='relu', input_shape=(192, 1)))
model.add(MaxPool1D(3))
# C2
model.add(Conv1D(filters=6, kernel_size=3, activation='relu'))
model.add(MaxPool1D(3))
# C3
model.add(Conv1D(filters=6, kernel_size=3, activation='relu'))
model.add(MaxPool1D(3))
# C4
model.add(Conv1D(filters=6, kernel_size=3, activation='relu'))
model.add(MaxPool1D(3))

model.add(Flatten())
# Fully-connected
model.add(Dense(12, activation='relu'))
model.add(Dense(len(cate_list), activation='softmax'))
model.summary()


train_label = np_utils.to_categorical(train_label, len(cate_list))


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

train_data = np.expand_dims(train_data, axis=-1)
# train_data = np_utils.to_categorical(train_data, 34)
# train_label = np_utils.to_categorical(train_label, 34)
# print(train_data)

# cp_callback = tf.keras.callbacks.ModelCheckpoint(
#     filepath=checkpoint_path_2,
#     verbose=1,
#     # save_weights_only=True,
#     period=5
# )
model.fit(train_data, train_label, batch_size=16, epochs=1000, verbose=1)

model_path = '../../model/model.h5'
model.save(model_path)

# model.predict()
