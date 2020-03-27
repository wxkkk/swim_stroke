import pandas as pd
import numpy as np
import constants


def window_data_txt(path, shuffle=False):
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
    # shuffle
    temp = np.array([data_wid, label_wid])
    temp = temp.transpose()
    if shuffle:
        np.random.shuffle(temp)

    data_list = list(temp[:, 0])
    label_list = list(temp[:, 1])

    return data_list, label_list


def window_data_csv(path, shuffle=True):
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

    # 组合list
    # data_wid_list = np.hstack((data_wid, ))

    # shuffle
    temp = np.array([data_wid, label_wid])
    temp = temp.transpose()
    if shuffle:
        np.random.shuffle(temp)

    # get data, label
    data_list = list(temp[:, 0])
    label_list = list(temp[:, 1])

    return data_list, label_list


def to_np(list_1, list_2):

    data_arr = np.zeros((len(list_1), constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1), dtype=np.uint8)
    label_arr = np.zeros((len(list_2), 1), dtype=np.uint8)

    for n in range(len(data_arr)):
        list_1[n] = np.resize(list_1[n], (constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1))
        list_2[n] = np.resize(list_2[n], 1)
        data_arr[n] = list_1[n]
        label_arr[n] = list_2[n]

    return data_arr, label_arr


def process_data_merge_txt_csv(path, shuffle=True, merge_txt_csv=True):

    list_csv_1, list_csv_2 = window_data_csv(path[0], shuffle)

    list_txt_1, list_txt_2 = window_data_txt(path[1], shuffle)

    if merge_txt_csv:
        list_csv_1.extend(list_txt_1)
        list_csv_2.extend(list_txt_2)

    data_arr, label_arr = to_np(list_csv_1, list_csv_2)

    return data_arr, label_arr


def process_data_txt(path, shuffle=True):

    list_1, list_2 = window_data_txt(path, shuffle)

    data_arr, label_arr = to_np(list_1, list_2)

    return data_arr, label_arr


def process_data_csv(path, shuffle=True):

    list_1, list_2 = window_data_csv(path, shuffle)

    data_arr, label_arr = to_np(list_1, list_2)

    return data_arr, label_arr

# test_csv_path = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_1_V2.csv'
#
# test_txt_path = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_2.txt'
# #
# test_path = [test_csv_path, test_txt_path]
# #

# d_a, l_a = process_data_csv(test_csv_path, False)
#
# print(len(d_a), np.squeeze(l_a))








