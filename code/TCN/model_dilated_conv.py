from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout, BatchNormalization
import constants
from TCN.tcn import TCN

''' dilated convolution]
    dilation = 1, 2, 4, ...
'''


def build_model():
    model = Sequential()

    # C1
    model.add(Conv2D(filters=16, kernel_size=(3, 1), strides=1, activation='relu', padding='valid', input_shape=constants.INPUT_SHAPE))
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.5))

    # C2
    model.add(Conv2D(filters=16, kernel_size=(3, 1), strides=2, activation='relu', padding='valid'))
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.25))

    # C3
    model.add(Conv2D(filters=16, kernel_size=(3, 1), strides=4, activation='relu', padding='valid'))
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.25))

    # C4
    # model.add(Conv2D(filters=16, kernel_size=(3, 1), strides=8, activation='relu', padding='valid'))
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.5))

    model.add(Flatten())
    # Fully-connected
    model.add(Dense(16, activation='relu'))
    # model.add(Dropout(0.5))
    model.add(Dense(len(constants.CATE_LIST), activation='softmax'))

    model.summary()

    return model


if __name__ == '__main__':
    build_model()

