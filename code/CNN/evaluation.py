import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.utils import to_categorical
import raw_data_to_window
import evaluation_show
import raw_data_to_h5


def evaluation_show_single(model, path):
    valid_files = os.listdir(path)

    for i, f in enumerate(valid_files):
        print('\n')
        print(f)
        f = os.path.join(path, f)
        valid_input, train_label = raw_data_to_window.process_data_csv_by_line(f, shuffle=False)

        predicted_results_class = model.predict_classes(valid_input)

        train_label = np.squeeze(train_label)
        print('truth count: ', len(train_label) - sum(train_label == 0), ',',
              'predicted count: ', len(predicted_results_class) - sum(predicted_results_class == 0))
        print('Truth label:     ', train_label)
        print('Predicted label: ', predicted_results_class)

        # plot predicted
        evaluation_show.show_plot(f, f, truth_lables=train_label, predicted_labels=predicted_results_class)


def evaluation_summary(model, path):
    valid_data, valid_label = raw_data_to_h5.read_h5(path)

    valid_label = to_categorical(valid_label)

    model.evaluate(valid_data, valid_label, verbose=2)


if __name__ == '__main__':
    valid_path_csv = r'../../data/test_data/seperate'
    valid_path_txt = r''

    valid_total = r'../generator_data/test_data/test.h5'

    model = tf.keras.models.load_model('../../model/TCN_model/202006191528.h5')

    model.summary()

    # evaluation_show_single(model, valid_path_csv)

    evaluation_summary(model, valid_total)
