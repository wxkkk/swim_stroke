from tensorflow.keras import Sequential, Input
from tensorflow.keras.layers import Dense, Dropout
from CNN import constants
from TCN.tcn import TCN


def build_model():
    model = Sequential()

    model.add(Input(shape=constants.INPUT_SHAPE))
    # model.add(Lambda(lambda y: K.reshape(y, (-1, h, w, c))))
    model.add(TCN(nb_filters=16,
                  kernel_size=6,
                  dilations=[1, 2, 4, 8, 16, 32, 64]))
    model.add(Dropout(0.5))

    # Fully-connected
    # model.add(Dropout(0.5))
    model.add(Dense(len(constants.CATE_LIST), activation='softmax'))

    model.summary()

    return model


if __name__ == '__main__':
    build_model()

