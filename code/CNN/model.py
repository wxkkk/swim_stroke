from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, BatchNormalization
from CNN import constants


def build_model():
    model = Sequential()

    # C1
    model.add(Conv2D(filters=2, kernel_size=(3, 1), activation='relu', padding='valid', input_shape=constants.INPUT_SHAPE))
    model.add(BatchNormalization())
    model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.5))

    # C2
    model.add(Conv2D(filters=4, kernel_size=(3, 1), activation='relu', padding='valid'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.25))

    # C3
    model.add(Conv2D(filters=4, kernel_size=(3, 1), activation='relu', padding='valid'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((3, 1)))
    # # model.add(Dropout(0.25))

    # C4
    # model.add(Conv2D(filters=128, kernel_size=(3, 1), activation='relu', padding='same'))
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

