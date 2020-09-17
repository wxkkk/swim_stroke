import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard
import time
import train_result_plot
from multi_len_CNN import constants, model
from multi_len_CNN.utils import raw_data_to_h5

train_path = r'../../data/train_data/20200917/20200917.h5'


if __name__ == '__main__':

    model = model.build_model()

    train_data, train_label = raw_data_to_h5.read_h5(train_path)
    train_label = to_categorical(train_label, len(constants.CATE_LIST))
    train_label = np.expand_dims(train_label, axis=-2)
    print('train_shape: ', train_data.shape, '\nlabels shape: ', train_label.shape)

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=[tf.keras.metrics.categorical_accuracy, tf.keras.metrics.Recall()])

    cur_time = int(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
    model_path = '../../model/CNN_model/{}.h5'.format(cur_time)
    log_name = '{}'.format(cur_time)

    model_saver = ModelCheckpoint(
        filepath=model_path,
        verbose=2,
        save_best_only=True
    )

    early_stopper = EarlyStopping(
        monitor='val_loss',
        min_delta=0,
        patience=100,
        verbose=2,
        mode='min',
        baseline=None,
        restore_best_weights=True
    )

    tensor_board = TensorBoard(log_dir=r'..\..\log\{}'.format(log_name))

    result = model.fit(train_data,
                       train_label,
                       batch_size=32,
                       callbacks=[model_saver, early_stopper, tensor_board],
                       validation_split=0.1,
                       verbose=2,
                       epochs=5000)

    train_result_plot.draw_result(result)