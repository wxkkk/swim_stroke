# swim stroke recognizition and counting

#### `constants.py`
* set constants
#### `clean_label_show.py`
* clean data
* tool for labelling on raw data
* visual data samples
#### `raw_data_to_windwo`
* process .csv or .txt into nparray using window length and repetitive rate setting in `constants.py`
#### `np_to_h5.py`
* save nparray into hdf5 file
#### `train_result_plot.py`
* using line chart to show training procedure
#### `elutaion_show.py`
* show predicted result(s) using plot
#### `model.py`
* model sturcture
#### `train.py`
* set dataset
* set auto saver for model
* set early stopper (inlucdeing mode, patience, and monitor)
* set tensorboard
* cross validation split
* loss function
* batch size
#### `evaluation.py`
* evaluation and show the predicted results