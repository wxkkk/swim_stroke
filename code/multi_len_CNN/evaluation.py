import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.utils import to_categorical
from multi_len_CNN.utils import raw_data_to_window, raw_data_to_h5
from multi_len_CNN.utils import evaluation_show
from multi_len_CNN import constants


def evaluation_show_single(model, path):
    valid_files = os.listdir(path)

    for i, f in enumerate(valid_files):
        print('\n')
        print(f)
        f = os.path.join(path, f)
        valid_input, train_label = raw_data_to_window.process_data_csv_by_line(f, shuffle=False)
        train_label = np.reshape(train_label, (train_label.shape[0] * train_label.shape[1], ))
        '''
        todo:
        1.implement repetitive window
        2.use the repetitive part to calculate the predicted labels as 1 only both part is 1
        3.concatenate windows into one
        '''
        predicted_results = model.predict(valid_input)
        predicted_results = np.argmax(predicted_results, axis=-1)
        predicted_results = np.reshape(predicted_results, (predicted_results.shape[0] * predicted_results.shape[1]))

        # train_label = np.squeeze(train_label)
        # print('truth count: ', len(train_label) - sum(train_label == 0), ',',
        #       'predicted count: ', len(predicted_results_class) - sum(predicted_results_class == 0))
        # print('Truth label:     ', train_label)
        # print('Predicted label: ', predicted_results_class)
        #
        # # plot predicted
        evaluation_show.show_plot(f, f, truth_lables=train_label, predicted_labels=predicted_results)


def evaluation_summary(model, path):
    valid_data, valid_label = raw_data_to_h5.read_h5(path)

    valid_label = to_categorical(valid_label, len(constants.CATE_LIST))
    valid_label = np.expand_dims(valid_label, axis=-2)

    model.evaluate(valid_data, valid_label, verbose=2)


if __name__ == '__main__':
    valid_path_csv = r'F:\wangpengfei\PycharmProjects\swim_stroke\data\train_data\20200917\test'
    # valid_path_txt = r''

    valid_total = r'../../data/train_data/20200916_test.h5'

    model = tf.keras.models.load_model('../../model/CNN_model/202009171714.h5')

    model.summary()

    evaluation_show_single(model, valid_path_csv)

    # evaluation_summary(model, valid_total)
