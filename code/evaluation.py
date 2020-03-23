import tensorflow as tf
import numpy as np
import os
from utils import window_process, visulization_results

# valid_path = r'../train_data/breaststroke_team1_left_61.csv'
valid_path = r'../data/valid_data'
valid_files = os.listdir(valid_path)

model = tf.keras.models.load_model('../model/202003231738.h5')

model.summary()

for i, f in enumerate(valid_files):
    print(f)
    f = os.path.join(valid_path, f)
    valid_input, train_label = window_process.process_data(f, False)

    predicted_results_class = model.predict_classes(valid_input)

    # predicted_results = model.predict(valid_input)
    # predicted_results = np.argmax(predicted_results, axis=-1)
    train_label = np.squeeze(train_label)
    print('truth count: ', len(train_label) - sum(train_label == 0), ',',
          'predicted count: ', len(predicted_results_class) - sum(predicted_results_class == 0))
    print('Truth label:     ', train_label)
    print('Predicted label: ', predicted_results_class)
    print('\n')

# valid[10] = predicted_results

# valid.to_csv('../data/validation_data/predicted/results.csv')
