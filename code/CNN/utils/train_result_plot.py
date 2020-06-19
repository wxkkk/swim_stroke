import matplotlib.pyplot as plt


def draw_result(results):
    # Draw MIoU
    plt.plot(results.history['categorical_accuracy'])
    plt.plot(results.history['val_categorical_accuracy'])
    plt.title('Model categorical_accuracy')
    plt.ylabel('categorical_accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # Draw Loss
    plt.plot(results.history['loss'])
    plt.plot(results.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()