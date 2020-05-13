import tensorflow as tf
import numpy as np
from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, LeakyReLU, Conv2DTranspose, Reshape
import constants


def make_swim_generator():
    model = Sequential()
    model.add(Dense(constants.GENERATED_NUM * 10 * 6 * 256, input_shape=(100,)))
    model.add(BatchNormalization())
    model.add(LeakyReLU())

    model.add(Reshape((constants.GENERATED_NUM * 10, 6, 256)))

    model.add(Conv2DTranspose(128, (3, 1), strides=(2, 1), padding='same'))
    model.add(BatchNormalization())

    model.add(Conv2DTranspose(64, (3, 1), strides=(2, 1), padding='same'))
    model.add(BatchNormalization())

    model.add(Conv2DTranspose(1, (3, 1), strides=(2, 1), padding='same'))
    assert model.output_shape == (None, constants.GENERATED_NUM * constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1)

    model.summary()

    return model


if __name__ == '__main__':
    make_swim_generator()
    # noise = tf.random.normal([1, 100])
    #
    # generator = make_swim_generator()
    #
    # generated = generator(noise)
    #
    # print(np.array(generated).shape)
