import pandas as pd
import numpy as np

train_path = r'../data/test_data/original/train.csv'

train_file = pd.read_csv(train_path)
print(train_file[50:100])
print(train_file[train_file['species'].str.contains('|', regex=False)])
train_file.drop(columns=['id'], inplace=True)
# train_file['species'] = train_file['species'].fillna('0')
train_file = train_file.reset_index()

# labels encode
# train_file.loc[train_file.species.str.contains('Acer'), 'species'] = str(0)
# train_file.loc[train_file.species.str.contains('Pterocarya'), 'species'] = '1'
cate_list = ['Acer', 'Pterocarya', 'Quercus', 'Tilia', 'Magnolia', 'Salix', 'Zelkova', 'Betula',
             'Fagus', 'Phildelphus', 'Populus', 'Alnus', 'Arundinaria', 'Liriodendron', 'Cytisus',
              'Rhododendron', 'Eucalyptus', 'Cercis', 'Cotinus', 'Celtis', 'Cornus', 'Callicarpa',
             'Prunus', 'Ilex', 'Ginkgo', 'Liquidambar', 'Lithocarpus', 'Viburnum', 'Crataegus',
             'Morus', 'Olea', 'Castanea', 'Ulmus', 'Sorbus']
print('cate counts:', len(cate_list))
for i in range(len(cate_list)):
    train_file.loc[train_file.species.str.contains(cate_list[i]), 'species'] = str(i)

# print(train_file.loc[train_file['species'] == '0'])
# print(train_file.head(20))
print(train_file.head(50))
train_file.to_csv('../data/test_data/processed/train_file.csv', index=False)
print(train_file.describe())

