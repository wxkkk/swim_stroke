import pandas as pd


def csv_data_reserved_aug(data, list):
    data.loc[:, list] = -1 * data.loc[:, list]

    return data


if __name__ == '__main__':
    data = pd.read_csv('../../data/train_data/train.csv', header=None)

    print(data)

    data_reversed = csv_data_reserved_aug(data, [0, 4, 5])

    print(data_reversed)