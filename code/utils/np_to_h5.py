import numpy as np
import h5py
import window_process


def process_data_to_np(path):
    d_a, l_a = window_process.process_data_merge_txt_csv(path, merge_txt_csv=True)
    print(len(d_a), np.squeeze(l_a))

    return d_a, l_a


def save_h5(data, labels, save_path):
    with h5py.File(save_path, 'w') as f:
        f['data'] = data
        f['labels'] = labels


def read_h5(path):
    with h5py.File(path, 'r') as f:
        data = np.array(f['data'])
        labels = np.array(f['labels'])

    return data, labels


if __name__ == '__main__':
    test_csv_path = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_1_V2.csv'
    test_txt_path = r'F:/wangpengfei/泳姿/swimming_stroke/swimming/data/processed/train_2.txt'
    merge_path = [test_csv_path, test_txt_path]

    h5_path = '../../data/train_data/train_set.h5'

    train_data, train_label = process_data_to_np(merge_path)
    save_h5(train_data, train_label, h5_path)
    train_data, train_label = read_h5(h5_path)
    print(train_data.shape, train_label.shape)
