---------------------
202003201445 
    train 0.98 valid 0.93
    shape (100, 6, 1)
    3 conv
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 128
    valid split 0.3
---------------------

---------------------
202003201738
    train 97.74% valid 93.11%
    shape (100, 6, 1)
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 128
    valid split 0.3
---------------------

---------------------
202003201817 X
    train null valid 93.59%
    shape (90, 6, 1)
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 128
    valid split 0.3
---------------------
---------------------
202003211106 (using 9 sensor parameters instead of 6)
    train 94.96% valid 93.69%
    shape (100, 9, 1)
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 128
    valid split 0.3
---------------------

---------------------
202003231738
    train 94.38% valid 93.40%
    shape (90, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 64
    valid split 0.3
---------------------

---------------------
202003240940
    train 95.53% valid 94.25%
    shape (80, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 64
    valid split 0.3
---------------------

---------------------
202003241012 normal
    train 94.90% valid 94.70%
    shape (90, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 32
    valid split 0.3
---------------------

validation loss from first time 30.xx% reduced to 17.xx after one week optimising

---------------------
202003241055 normal
    train 93.49% valid 94.64%
    train_loss 0.1877 valid_loss 0.1735
    shape (80, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 16
    valid split 0.3
---------------------

---------------------
202003241137 good
    train 95.80% valid 95.38%
    train_loss 0.1221 valid_loss 0.1712
    shape (80, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.25, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 16
    valid split 0.1
---------------------

---------------------
202003241537 good
    train 92.59% valid 95.06%
    train_loss 0.2146 valid_loss 0.1555
    shape (80, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.5, 0.5, 0.5
    padding valid, valid, valid
    dense 128
    batch 16
    valid split 0.1
---------------------

---------------------
202003241834 good+
    train 95.48% valid 95.98%
    train_loss 0.1265 valid_loss 0.1484
    recall 0.9508 valid_recall 0.9566
    shape (80, 9, 1)
    repetitive rate 40%
    3 conv 
    batchnormalization *3
    filters 32, 32, 32
    maxpooling 3*1, 3*1, 3*1
    dropout 0.5, 0.5, 0.25, 0.25
    padding valid, valid, valid
    dense 128
    batch 16
    valid split 0.1
---------------------
the following model were using train_1_V2 and train_2 training
---------------------

---------------------
202003261234 
    valid 84.01%
---------------------

---------------------
the following model starting training since 20200528
---------------------

---------------------
202005291136
    train 96.24% valid 96.28%
    train_loss 0.1278 valid_loss 0.1276
    recall 0.9602 valid_recall 0.9577
    shape (90, 6, 1)
    repetitive rate 20%
    3 conv 
    batchnormalization -
    filters 2, 4, 1
    maxpooling 3*1, 3*1, 3*1
    dropout -
    padding valid, valid, valid
    dense 32
    batch 128
    valid split 0.1
---------------------
