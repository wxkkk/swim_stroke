import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, TensorBoard
import time
from utils import window_process, visulization_results

cate_list = ['unknown', 'freestyle', 'breaststroke', 'butterfly', 'backstroke']

train_path = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_1_V2.csv'

model = Sequential()
input_shape = (80, 9, 1)
# C1
model.add(Conv2D(filters=32, kernel_size=(3, 1), activation='elu', padding='valid', input_shape=input_shape))
model.add(BatchNormalization())
model.add(MaxPool2D((3, 1)))
model.add(Dropout(0.5))
# C2
model.add(Conv2D(filters=32, kernel_size=(3, 1), activation='elu', padding='valid'))
model.add(BatchNormalization())
model.add(MaxPool2D((3, 1)))
model.add(Dropout(0.5))
# C3
model.add(Conv2D(filters=32, kernel_size=(3, 1), activation='elu', padding='valid'))
model.add(BatchNormalization())
model.add(MaxPool2D((3, 1)))
model.add(Dropout(0.5))
# C4
# model.add(Conv2D(filters=64, kernel_size=(3, 1), activation='elu', padding='valid'))
# model.add(BatchNormalization())
# model.add(Dropout(0.5))

model.add(Flatten())
# Fully-connected
model.add(Dense(128, activation='elu'))
model.add(Dropout(0.5))
model.add(Dense(len(cate_list), activation='softmax'))

model.summary()

# train_label = np_utils.to_categorical(train_label, len(cate_list))
train_data, train_label = window_process.process_data(train_path)

print('train_shape: ', train_data.shape)
train_label = to_categorical(train_label, len(cate_list))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=[tf.keras.metrics.categorical_accuracy, tf.keras.metrics.Recall()])


cur_time = int(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
model_path = '../model/{}.h5'.format(cur_time)
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

tensor_board = TensorBoard(log_dir=r'..\log\{}'.format(log_name))

result = model.fit(train_data,
                   train_label,
                   batch_size=16,
                   callbacks=[model_saver, early_stopper, tensor_board],
                   validation_split=0.1,
                   verbose=2,
                   epochs=5000)

visulization_results.draw_result(result)
