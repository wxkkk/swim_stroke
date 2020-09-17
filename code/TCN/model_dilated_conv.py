from tensorflow.keras import Sequential, Input, Model
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Conv2DTranspose, concatenate
from CNN import constants

''' dilated convolution]
    dilation = 1, 2, 4, ...
'''


def build_model():

    inputs = Input(shape=constants.INPUT_SHAPE)

    C1 = Conv2D(filters=2, kernel_size=(3, 1), strides=(1, 1), activation='relu', padding='valid')(inputs)
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.5))

    C2 = Conv2D(filters=4, kernel_size=(3, 1), strides=(2, 1), activation='relu', padding='valid')(C1)
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.25))

    C3 = Conv2D(filters=8, kernel_size=(3, 1), strides=(4, 1), activation='relu', padding='valid')(C2)
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.25))

    # C4 = Conv2D(filters=16, kernel_size=(3, 1), strides=(8, 1), activation='relu', padding='valid')(C3)
    # model.add(BatchNormalization())
    # model.add(MaxPool2D((3, 1)))
    # model.add(Dropout(0.5))

    F = Flatten()(C3)
    # Fully-connected
    F1 = Dense(16, activation='relu')(F)
    # model.add(Dropout(0.5))
    outputs = Dense(len(constants.CATE_LIST), activation='softmax')(F1)

    model = Model(inputs=[inputs], outputs=[outputs])

    model.summary()

    return model


if __name__ == '__main__':
    build_model()

