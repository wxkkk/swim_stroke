import pandas as pd
import numpy as np
from CNN import constants
import data_augmentation


def window_data_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines_len = len(lines)
        x = np.zeros(shape=(lines_len, 9))
        y = np.zeros(shape=(lines_len,))

        for i in range(lines_len):
            ns = lines[i][lines[i].find('[')+1: lines[i].find(']')].split(',')
            # input number of sensor parameters
            for j in range(constants.SENSOR_PARAMETERS - 1):
                x[i, j] = float(ns[j])
            y[i] = int(ns[9])

    data_wid = []
    label_wid = []
    for i in range(1, int(len(x) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
        i *= int(constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE))
        # print(i)
        data_wid_temp = x[i:i + constants.WINDOW_LENGTH - 1]
        label_wid_temp = max(y[i:i + constants.WINDOW_LENGTH - 1].astype(int))

        data_wid.append(data_wid_temp)
        label_wid.append(label_wid_temp)

    return data_wid, label_wid


def window_data_csv(path):
    data = pd.read_csv(path)
    data = data.dropna()
    data_wid = []
    label_wid = []
    for i in range(1, int(len(data) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
        i *= int(constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE))
        # print(i)
        data_wid_temp = data.loc[i:i + constants.WINDOW_LENGTH - 1, ['1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0']]
        label_wid_temp = max(data.loc[i:i + constants.WINDOW_LENGTH - 1, '0'].astype(int))

        data_wid.append(data_wid_temp)
        label_wid.append(label_wid_temp)

    return data_wid, label_wid


def window_data_csv_by_line(path, augmentation=False):

    data = pd.read_csv(path, header=None)
    data.dropna()
    # print(generator_data.columns.values)

    data_wid = []
    label_wid = []
    count = 0

    for i in range(int(len(data) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
        i *= constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE)
        # print(i)
        data_wid.append(data.loc[i: i + constants.WINDOW_LENGTH - 1, [0, 1, 2, 3, 4, 5]])
        label_wid.append(max(data.loc[i: i + constants.WINDOW_LENGTH - 1, 9]))
        count += 1

    if augmentation:
        data_reversed_aug = data_augmentation.csv_data_reserved_aug(data, [0, 4, 5])

        for i in range(int(len(data_reversed_aug) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
            i *= constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE)
            data_wid.append(data_reversed_aug.loc[i: i + constants.WINDOW_LENGTH - 1, [0, 1, 2, 3, 4, 5]])
            label_wid.append(max(data_reversed_aug.loc[i: i + constants.WINDOW_LENGTH - 1, 9]))
            count += 1

    print('count: ', count)

    return data_wid, label_wid


def to_np(data_wid, label_wid, shuffle=True):

    # 组合list
    # data_wid_list = np.hstack((data_wid, ))

    # shuffle
    temp = np.array([data_wid, label_wid])
    temp = temp.transpose()
    if shuffle:
        np.random.shuffle(temp)

    # get generator_data, label
    data_list = list(temp[:, 0])
    label_list = list(temp[:, 1])

    data_arr = np.zeros((len(data_list), constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1), dtype=np.float64)
    label_arr = np.zeros((len(label_list), 1), dtype=np.uint8)

    for n in range(len(data_arr)):
        data_arr[n] = np.resize(data_list[n], (constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1))
        label_arr[n] = np.resize(label_list[n], 1)

    return data_arr, label_arr


def process_data_merge_txt_csv(path, shuffle=True, merge_txt_csv=True):

    list_csv_1, list_csv_2 = window_data_csv(path[0])

    list_txt_1, list_txt_2 = window_data_txt(path[1])

    if merge_txt_csv:
        list_csv_1.extend(list_txt_1)
        list_csv_2.extend(list_txt_2)

    data_arr, label_arr = to_np(list_csv_1, list_csv_2, shuffle)

    return data_arr, label_arr


def process_data_txt(path, shuffle=True):

    list_1, list_2 = window_data_txt(path)

    data_arr, label_arr = to_np(list_1, list_2, shuffle)

    return data_arr, label_arr


def process_data_csv(path, shuffle=True):

    list_1, list_2 = window_data_csv(path)

    data_arr, label_arr = to_np(list_1, list_2, shuffle)

    return data_arr, label_arr


def process_data_csv_by_line(path, shuffle=True, augmentation=False):

    list_1, list_2 = window_data_csv_by_line(path, augmentation)

    data_arr, label_arr = to_np(list_1, list_2, shuffle)

    return data_arr, label_arr


if __name__ == '__main__':
    train_path_csv = r'F:\wangpengfei\PycharmProjects\untitled\data\test_mereged\merged.csv'
    train_path_txt = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_2.txt'

    train_path = [train_path_csv, train_path_txt]
    
    d_a, l_a = process_data_csv_by_line(train_path[0], True)

    print(len(d_a), np.squeeze(l_a))








