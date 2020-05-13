import pandas as pd
import numpy as np
import h5py
import constants


def process_to_slice_window():
    path = '../data/Freestyle_1531758722314.csv'
    data = pd.read_csv(path, header=None)
    data.dropna()
    # print(data.head())
    print(data.columns.values)
    # print(data.loc[:80, 1])
    data_wid = []
    label_wid = []
    count = 0

    for i in range(int(len(data) // constants.WINDOW_LENGTH // (1 - constants.WINDOW_REPETITIVE_RATE))):
        i *= constants.WINDOW_LENGTH * (1 - constants.WINDOW_REPETITIVE_RATE)
        # print(i)
        data_wid.append(data.loc[i: i + constants.WINDOW_LENGTH - 1, [0, 1, 2, 3, 4, 5]])
        label_wid.append(max(data.loc[i: i + constants.WINDOW_LENGTH - 1, 9]))
        count += 1

    print('count: ', count)
    # print(data_wid[3])
    # print(label_wid)
    temp = np.array([data_wid, label_wid])
    temp = temp.transpose()
    np.random.shuffle(temp)
    # get data, label
    data_list = list(temp[:, 0])
    label_list = list(temp[:, 1])
    data_arr = np.zeros((len(data_list), constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1), dtype=np.float)
    label_arr = np.zeros((len(label_list), 1), dtype=np.uint8)
    for n in range(len(data_arr)):
        data_arr[n] = np.resize(data_list[n], (constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1))
        label_arr[n] = np.resize(label_list[n], 1)
    h5_path = '../data/test_generator.h5'
    with h5py.File(h5_path, 'w') as f:
        f['data'] = data_arr
        f['labels'] = label_arr


def read_h5(path):
    with h5py.File(path, 'r') as f:
        data = np.array(f['data'])
        labels = np.array(f['labels'])

    return data, labels


if __name__ == '__main__':
    process_to_slice_window()
