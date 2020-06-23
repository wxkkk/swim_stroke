import numpy as np
from tensorflow.keras import backend as K, Sequential, Input, Model
from tensorflow.keras.layers import Conv2D, Dense, Dropout, Lambda, MaxPool2D
from CNN import constants
from TCN.tcn import TCN


def build_model():

    inputs = Input(shape=constants.INPUT_SHAPE)

    # x = Conv2D(filters=16, kernel_size=(3, 1), padding='valid')(inputs)
    # x = MaxPool2D()(x)

    num_features_cnn = np.prod(K.int_shape(inputs)[1:])
    x = Lambda(lambda y: K.reshape(y, (-1, 1, num_features_cnn)))(inputs)

    x = TCN(kernel_size=6, nb_filters=16, dilations=(1, 2, 4, 8), use_skip_connections=True)(x)

    x = Dense(len(constants.CATE_LIST), activation='softmax')(x)

    model = Model(inputs=[inputs], outputs=[x])

    model.summary()

    return model


if __name__ == '__main__':
    build_model()

