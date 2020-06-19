import numpy as np
import h5py
import raw_data_to_window


def process_data_to_np(path):
    d_a, l_a = raw_data_to_window.process_data_merge_txt_csv(path, merge_txt_csv=True)
    print(len(d_a), np.squeeze(l_a))

    return d_a, l_a


def save_h5(data, labels, save_path):
    with h5py.File(save_path, 'w') as f:
        f['generator_data'] = data
        f['labels'] = labels


def read_h5(path):
    with h5py.File(path, 'r') as f:
        data = np.array(f['generator_data'])
        labels = np.array(f['labels'])

    return data, labels


if __name__ == '__main__':
    csv_path = r'../../../data/train_data/train_walk.csv'
    # txt_path = r'F:\wangpengfei\PycharmProjects\untitled\generator_data\labelled\train_set_V1_2.txt'
    # merge_path = [csv_path, txt_path]

    train_data, train_label = raw_data_to_window.process_data_csv_by_line(csv_path, augmentation=True)
    h5_path = r'../../data/train_data/train_walk.h5'

    save_h5(train_data, train_label, h5_path)
    # train_data, train_label = read_h5(h5_path)
    # print(train_data.shape, train_label.shape)
