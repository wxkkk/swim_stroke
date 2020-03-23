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