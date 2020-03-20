import pandas as pd
import numpy as np

window_length = 100


def window_data(path, shuffle=True):
    data = pd.read_csv(path)
    data = data.dropna()
    data_wid = []
    label_wid = []
    for i in range(1, (len(data) // window_length) * 2):
        i *= window_length // 2
        # print(i)
        data_wid_temp = data.loc[i:i + window_length - 1, ['1.0', '2.0', '3.0', '4.0', '5.0', '6.0']]
        label_wid_temp = max(data.loc[i:i + window_length - 1, '0'].astype(int))

        data_wid.append(data_wid_temp)
        label_wid.append(label_wid_temp)
        # data_wid.append(data.loc[i:i + 179, ['1', '2', '3', '4', '5', '6']])
        # label_wid.append(max(data.loc[i:i + 179, '0']))
        # print('data:\n', data_wid)
        # print('label:\n', label_wid)
        # print(i)
        # np.save()

    # 组合list
    # data_wid_list = np.hstack((data_wid, ))

    # shuffle 打乱
    # print(label_wid)
    temp = np.array([data_wid, label_wid])
    temp = temp.transpose()
    if shuffle:
        np.random.shuffle(temp)

    # 取出data、label
    data_list = list(temp[:, 0])
    label_list = list(temp[:, 1])

    return data_list, label_list


def to_np(list_1, list_2):

    data_arr = np.zeros((len(list_1), window_length, 6, 1), dtype=np.uint8)
    label_arr = np.zeros((len(list_2), 1), dtype=np.uint8)

    for n in range(len(data_arr)):
        list_1[n] = np.resize(list_1[n], (window_length, 6, 1))
        list_2[n] = np.resize(list_2[n], 1)
        data_arr[n] = list_1[n]
        label_arr[n] = list_2[n]
    # print(label_arr)
    # print(data_arr[0][0])
    # print(len(data_list), len(label_list))
    # data_arr, label_arr = np.array(list_1), np.array(list_2)
    # print(data_arr)
    # print(label_arr)
    # print(data_arr.shape, label_arr.shape)

    return data_arr, label_arr


def process_data(path, shuffle=True):

    list_1, list_2 = window_data(path, shuffle)

    data_arr, label_arr = to_np(list_1, list_2)

    return data_arr, label_arr


# train_path = r'../train_data/merged.csv'
#
# input_path = r'../data/valid_data/freestyle_team1_left_01.csv'
#
# d_a, l_a = process_data(input_path)
#
# print(len(d_a), l_a)

#
# print('data:\n', csv_file.loc[1130:1140, ['1', '2', '3', '4', '5', '6']])
#
# print('label:\n', csv_file.loc[1130:1140, '0'])
#
# print(len(csv_file) // 180)
#
# print(window_data(input_path))






