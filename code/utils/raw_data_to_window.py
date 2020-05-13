import pandas as pd
import numpy as np
import csv
import constants


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


def window_data_csv_by_line(path):
    with open(path, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        result = list(reader)
        data_wid = []
        label_wid = []
        x = np.zeros(shape=(len(result), 9))
        y = np.zeros(shape=(len(result),))

        for row_num in range(1, int(len(result) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
            row_num *= int(constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE))
            print(row_num)
            for col_num in range(9):
                x[row_num, col_num] = float(result[row_num][col_num])
            y[row_num] = int(result[row_num][9])

            data_wid.append(result[row_num:row_num + constants.WINDOW_LENGTH - 1])
            label_wid.append(max(y[row_num:row_num + constants.WINDOW_LENGTH - 1].astype(int)))

    return data_wid, label_wid


def to_np(data_wid, label_wid, shuffle=True):

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

    data_arr = np.zeros((len(data_list), constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1), dtype=np.uint8)
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


def process_data_csv_by_line(path, shuffle=True):

    list_1, list_2 = window_data_csv_by_line(path)

    data_arr, label_arr = to_np(list_1, list_2, shuffle)

    return data_arr, label_arr


if __name__ == '__main__':
    train_path_csv = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_1_V2.csv'
    train_path_txt = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_2.txt'

    train_path = [train_path_csv, train_path_txt]
    
    d_a, l_a = process_data_merge_txt_csv(train_path, True)

    print(len(d_a), np.squeeze(l_a))








