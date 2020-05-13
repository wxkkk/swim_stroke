import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Conv2D, Dropout, Flatten, Dense
import constants


def make_swim_dis():
    model = Sequential()
    # C1
    model.add(Conv2D(filters=64, kernel_size=(3, 1), activation='relu', padding='valid',
                     input_shape=constants.INPUT_SHAPE))
    model.add(Dropout(0.5))
    # C2
    model.add(Conv2D(filters=64, kernel_size=(3, 1), activation='relu', padding='valid'))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(layers.Dense(1))

    model.summary()

    return model


if __name__ == '__main__':
    make_swim_dis()
