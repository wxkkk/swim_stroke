import tensorflow as tf
import numpy as np
import os
import raw_data_to_window
import evaluation_show

valid_path_csv = r'F:\wangpengfei\PycharmProjects\untitled\data\test_plot'
valid_path_txt = r'F:\wangpengfei\泳姿\swimming_stroke\swimming\data\processed\test'


valid_files = os.listdir(valid_path_csv)

model = tf.keras.models.load_model('../model/202005281715.h5')

model.summary()

for i, f in enumerate(valid_files):
    print('\n')
    print(f)
    f = os.path.join(valid_path_csv, f)
    valid_input, train_label = raw_data_to_window.process_data_csv_by_line(f, shuffle=False)

    predicted_results_class = model.predict_classes(valid_input)

    train_label = np.squeeze(train_label)
    print('truth count: ', len(train_label) - sum(train_label == 0), ',',
          'predicted count: ', len(predicted_results_class) - sum(predicted_results_class == 0))
    print('Truth label:     ', train_label)
    print('Predicted label: ', predicted_results_class)

    # plot predicted
    evaluation_show.show_plot(f, f, predicted_results_class)

