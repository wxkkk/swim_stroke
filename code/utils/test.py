import time
import calendar

import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import keras
# from utils import window_process

# train_path = r'../data/test_data/original'
# train = pd.read_csv(train_path + '/train.csv')
# test = pd.read_csv(train_path + '/test.csv')
#
# def encode(train, test):
#     label_encoder = LabelEncoder().fit(train.species)
#     labels = label_encoder.transform(train.species)
#     classes = list(label_encoder.classes_)
#
#     train = train.drop(['species', 'id'], axis=1)
#     test = test.drop('id', axis=1)
#
#     return train, labels, test, classes
#
# train, labels, test, classes = encode(train, test)
#
# print(train, labels, test, classes)

# fashion_data = keras.datasets.fashion_mnist
#
# (train_images, train_labels), (test_images, test_labels) = fashion_data.load_data()
# print(train_images, train_labels)

# print(time.localtime(time.time()))
# print(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
print(int(4000 // 90 // 0.3 ))