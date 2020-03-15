import keras
import pandas as pd
import numpy as np
from utils import window_process

# input_path = r'../train_data/freestyle_team1_left_01.csv'

valid_path = r'../train_data/breaststroke_team1_left_61.csv'
# valid = pd.read_csv(valid_path)
# valid = valid[valid.columns.values[1:10]]
# valid_input = np.expand_dims(valid, axis=-1)

model = keras.models.load_model('../model/model.h5')

model.summary()

valid_input, train_label = window_process.process_data(valid_path)

predicted_results_class = model.predict_classes(valid_input)

# predicted_results = model.predict(valid_input)
# predicted_results = np.argmax(predicted_results, axis=-1)

print(len(predicted_results_class))
print('Truth label: ', train_label)
print('Predicted label: ', predicted_results_class)

# valid[10] = predicted_results

# valid.to_csv('../data/validation_data/predicted/results.csv')
